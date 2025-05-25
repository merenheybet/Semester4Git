# Test-Suite für Hausaufgaben im Fach Algorithmik kontinuierlicher Systeme
#
# Version 2025.05.07
#
# Copyright © 2025 Frederik Hennig
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Sequence, Generator, Callable
from dataclasses import dataclass, field
from pathlib import Path
from fractions import Fraction
import multiprocessing as mp
from textwrap import indent
from collections import defaultdict
import numpy as np
import ast


TIMEOUT = 15
FLOAT_ATOL = 1e-12
FLOAT_RTOL = 1e-6


class PrettyPrint:
    @staticmethod
    def wrap_detail(detail: str) -> str:
        return indent(detail, "  > ", lambda _: True)

    @staticmethod
    def h1(text: str) -> str:
        return f"[   {text}   ]".center(81, "=") + "\n"

    @staticmethod
    def h2(text: str) -> str:
        return f"[   {text}   ]".center(81, "-") + "\n"


class MarkdownPrint:
    def __init__(self, block_depth: int = 3) -> None:
        self._block_depth: int = block_depth

    def admonition(self, kind: str, title: str, body: str, dropdown: bool = True):
        colons = ":" * self._block_depth
        md = colons + f"{{{kind}}} {title}\n"
        if dropdown:
            md += ":class: dropdown\n"
        md += "\n" + body + "\n"
        md += colons

        return md

    def status(self, title: str, body: str, dropdown: bool = True):
        return self.admonition("note", title, body, dropdown)

    def success(self, title: str, body: str, dropdown: bool = True):
        return self.admonition("hint", title, body, dropdown)

    def failure(self, title: str, body: str, dropdown: bool = True):
        return self.admonition("error", title, body, dropdown)


@dataclass(frozen=True)
class TestCase:
    args: tuple[Any]
    """Positional arguments to the function under test"""

    expected: Any
    """Expected result of the function under test"""


@dataclass
class Subtask:
    id: str
    """Subtask ID"""

    marks: Fraction
    """Marks alloted for this subtask"""

    function_name: str
    """Name of the function implementing this task"""

    description: str = ""
    """Subtask description"""

    test_cases: list[TestCase] = field(default_factory=list)
    """Test cases for this subtask"""


@dataclass
class Task:
    id: int
    """Task ID"""

    module: str
    """Module containing this task's solutions."""

    description: str = ""
    """This task's description"""

    subtasks: list[Subtask] = field(default_factory=list)
    """Set of subtasks of this task."""

    allowed_imports: set[str] = field(default_factory=set)
    """Modules that are allowed to be imported in this task."""

    monkeypatches: tuple[Callable, ...] = ()
    """Monkeypatches applied before each test run in this task"""

    def total_marks(self) -> Fraction:
        return sum((subt.marks for subt in self.subtasks), start=Fraction(0))


@dataclass
class Sheet:
    id: int
    """Exercise sheet number"""

    description: str = ""
    """Exercise sheet description"""

    tasks: list[Task] = field(default_factory=list)
    """Tasks on this sheet"""

    def get_task(self, id: int):
        return self.tasks[id - 1]


@dataclass
class TestResult:
    success: bool

    detail: str | None = None

    def string(self, verbose: bool = False) -> str:
        if self.success:
            outp = "Erfolgreich!"
        else:
            outp = "Fehler!"

        if self.detail and (verbose or not self.success):
            outp += "\n" + PrettyPrint.wrap_detail(self.detail)

        return outp

    def markdown(self, idx: int) -> str:
        p = MarkdownPrint(block_depth=3)

        title = f"Test {idx} - "
        body = f"```\n{self.detail}\n```"

        if self.success:
            title += "OK"
            return p.success(title, body)
        else:
            title += "Fehler"
            return p.failure(title, body)


@dataclass
class SubtaskReport:
    subtask: Subtask

    success: bool = False

    test_results: list[TestResult] = field(default_factory=list)

    marks: Fraction | None = None

    @property
    def _title(self) -> str:
        return f"Teilaufgabe {self.subtask.id}: {self.subtask.description}"

    @property
    def _marks_report(self) -> str:
        return f"{float(self.marks):g} / {float(self.subtask.marks):g} Punkte"

    def string(self, verbose: bool = False) -> str:
        outp = ""
        outp += PrettyPrint.h2(self._title)

        if verbose or not self.success:
            outp += "\n"
            outp += "\n".join(
                f"Test {i + 1}: {res.string(verbose)}"
                for i, res in enumerate(self.test_results)
            )
            outp += "\n"

        if self.success:
            outp += "\nAlle Tests Bestanden!\n\n"

        outp += PrettyPrint.h2(self._marks_report)

        return outp

    def markdown(self) -> str:
        title = f"{self._title} [{self._marks_report}]"
        p = MarkdownPrint(block_depth=4)

        body = "\n\n".join(tc.markdown(i) for i, tc in enumerate(self.test_results))

        if self.success:
            title = f"[OK] {title}"
            return p.success(title, body)
        else:
            title = f"[FEHLER] {title}"
            return p.failure(title, body)


@dataclass
class TaskReport:
    task: Task

    subtask_reports: dict[str, SubtaskReport] = field(default_factory=dict)

    error_msg: str | None = None
    marks: Fraction | None = None

    def add_marks(self) -> TaskReport:
        self.marks = Fraction(0)

        for subrep in self.subtask_reports.values():
            if subrep.success:
                assert subrep.marks is not None
                self.marks += subrep.marks

        return self

    @property
    def _title(self) -> str:
        return f"Aufgabe {self.task.id}: {self.task.description}"

    @property
    def _marks_report(self) -> str:
        max_marks = self.task.total_marks()
        return f"{float(self.marks):g} / {float(max_marks):g} Punkte"

    def string(self, verbose: bool = False) -> str:
        outp = "\n"
        outp += PrettyPrint.h1(self._title)

        if self.error_msg:
            outp += "\n" + self.error_msg + "\n"
        else:
            outp += "\n" + "\n\n".join(
                rep.string(verbose) for rep in self.subtask_reports.values()
            )

        outp += "\n"
        outp += PrettyPrint.h1(f"Aufgabe {self.task.id}: " + self._marks_report)

        return outp

    def markdown(self) -> str:
        p = MarkdownPrint(block_depth=5)
        title = f"{self._title} [{self._marks_report}]"
        if self.error_msg:
            title = f"[FEHLER] {title}"
            body = "```\n" + self.error_msg + "\n```"
            return p.failure(title, body, dropdown=False)

        else:
            body = "\n\n".join(st.markdown() for st in self.subtask_reports.values())
            return p.status(title, body, dropdown=False)


class ForbiddenMember:
    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return f"'{self._name}' darf in dieser Aufgabe nicht genutzt werden."

    def __repr__(self):
        return str(self)

    def __call__(self, *args, **kwargs):
        raise RuntimeError(str(self))

    def __getattr__(self, name: str) -> Any:
        raise RuntimeError(str(self))


@dataclass
class ev:
    """Wrapper around a code string that should be evaluated
    in the context of the module-under-test."""

    code: str


@dataclass
class tolerance:
    """Wrapper around an expected result specifying
    floating-point error tolerances to use in equality checking."""

    obj: Any
    atol: float
    rtol: float


class TaskRunner:

    class AstInspector(ast.NodeVisitor):
        def __init__(self, import_whitelist: set[str]):
            self._import_whitelist = import_whitelist
            self.errors: list[str] = []

        def check_module(self, module):
            if module not in self._import_whitelist:
                self.errors.append(
                    f"Das Modul '{module}' darf in dieser Aufgabe nicht verwendet werden."
                )

        def visit_Import(self, node):
            for m in [n.name for n in node.names]:
                self.check_module(m)

        def visit_ImportFrom(self, node):
            self.check_module(node.module)

    @dataclass
    class TestExecSpec:
        test_case: TestCase
        function_name: str
        module_name: str
        module_path: Path
        monkeypatches: tuple[Callable, ...]

    def __init__(self, task: Task, src_dir: Path, mp_context):
        self._task = task
        self._subtasks = {t.id: t for t in task.subtasks}
        self._src_dir = src_dir
        self._mp_context = mp_context

        self._modname = self._task.module
        self._py_filename = f"{self._modname}.py"
        self._modpath = self._src_dir / self._py_filename

        self._report: TaskReport = TaskReport(task)

    @property
    def report(self) -> TaskReport:
        return self._report

    def import_and_check(self) -> bool:
        """Import task module and perform static checks."""
        import importlib.util as iutil

        modspec = iutil.spec_from_file_location(self._modname, self._modpath)

        if modspec is None:
            self._report = TaskReport(
                self._task,
                error_msg=f"[FEHLER] Die Datei {self._modpath} konnte nicht gefunden werden",
                marks=Fraction(0),
            )
            return False

        module = iutil.module_from_spec(modspec)
        try:
            modspec.loader.exec_module(module)
        except Exception as e:
            self._report = TaskReport(
                self._task,
                error_msg=f"[FEHLER] Das Modul {self._modname} konnte nicht importiert werden:\n"
                + PrettyPrint.wrap_detail(repr(e)),
                marks=Fraction(0),
            )
            return False

        self._module = module

        module_code = self._modpath.read_text(encoding="utf-8")
        module_ast = ast.parse(module_code, self._modpath)
        inspector = TaskRunner.AstInspector(self._task.allowed_imports)
        inspector.visit(module_ast)
        if inspector.errors:
            msg = "\n".join(f"[FEHLER] {e}" for e in inspector.errors)
            self._report = TaskReport(self._task, error_msg=msg, marks=Fraction(0))
            return False

        return True

    def test_subtask(self, subtask_id: str) -> SubtaskReport:
        subtask = self._subtasks[subtask_id]
        subtask_report = SubtaskReport(subtask)

        from multiprocessing.pool import AsyncResult

        def consume(promise: AsyncResult) -> TestResult:
            try:
                return promise.get(timeout=TIMEOUT)
            except mp.TimeoutError:
                return TestResult(
                    success=False,
                    detail=f"Timeout: Der Test hat nach {TIMEOUT} Sekunden "
                    "kein Ergebnis erzielt und wurde abgebrochen.",
                )
            except BaseException as e:
                return TestResult(
                    success=False,
                    detail=f"Beim Ausführen des Tests ist ein Fehler aufgetreten: {e}",
                )

        with self._mp_context.Pool() as pool:
            promises = [
                pool.apply_async(
                    TaskRunner._exec_testcase,
                    (
                        TaskRunner.TestExecSpec(
                            tcase,
                            subtask.function_name,
                            self._modname,
                            self._modpath,
                            self._task.monkeypatches,
                        ),
                    ),
                )
                for tcase in subtask.test_cases
            ]

            results = [consume(promise) for promise in promises]

        subtask_report.test_results = results

        if all(r.success for r in results):
            subtask_report.success = True
            subtask_report.marks = subtask.marks
        else:
            subtask_report.success = False
            subtask_report.marks = Fraction(0)

        self._report.subtask_reports[subtask_id] = subtask_report
        return subtask_report

    @staticmethod
    def _exec_testcase(spec: TestExecSpec) -> TestResult:
        import importlib.util as iutil

        modspec = iutil.spec_from_file_location(spec.module_name, spec.module_path)
        assert modspec is not None
        module = iutil.module_from_spec(modspec)

        for mpatch in spec.monkeypatches:
            mpatch()

        try:
            modspec.loader.exec_module(module)  # type: ignore

            func = getattr(module, spec.function_name)

            args = tuple(
                (eval(arg.code, vars(module)) if isinstance(arg, ev) else arg)
                for arg in spec.test_case.args
            )

            outp = func(*args)

        except BaseException as e:
            return TestResult(False, str(e))

        success, err_msg = TaskRunner.check_result(outp, spec.test_case.expected)

        args_str = ", ".join(repr(arg) for arg in args)
        detail = f"{spec.function_name}({args_str}) = {repr(outp)}"
        if err_msg is not None:
            detail += "\n" + indent(err_msg, "  ", lambda _: True)

        return TestResult(success, detail)

    @staticmethod
    def check_result(actual: Any, expected: Any) -> tuple[bool, str | None]:
        error_detail: str | None = None

        float_atol = FLOAT_ATOL
        float_rtol = FLOAT_RTOL

        match expected:
            case ev(code):
                expected = eval(code)
            case tolerance(obj, atol, rtol):
                expected = obj
                float_atol = atol
                float_rtol = rtol

        if actual is None:
            error_detail = "Die Funktion gibt keinen Wert zurück."

        #   Check types
        if error_detail is None:
            match expected:
                case np.ndarray():
                    if not isinstance(actual, np.ndarray):
                        error_detail = (
                            f"Falscher Rückgabetyp: {type(actual).__name__}. "
                            "Erwartet wurde ein NumPy-Array."
                        )
                    if actual.shape != expected.shape:
                        error_detail = (
                            f"Falsche Array-Größe: {actual.shape}. "
                            f"Erwartet wurde {expected.shape}"
                        )
                case np.generic():
                    actual_type = type(actual)
                    expected_type = type(expected)
                    if actual_type is not expected_type:
                        error_detail = (
                            f"Falscher Rückgabetyp: {actual_type.__name__}. "
                            f"Erwartet wurde {expected_type.__name__}"
                        )
                case _:
                    #   Other non-NumPy type expected
                    if isinstance(actual, np.generic):
                        #   User return value is a numpy scalar -> get Python scalar type instead
                        actual_type = type(actual.item())
                    else:
                        actual_type = type(actual)

                    expected_type = type(expected)
                    if actual_type is not expected_type:
                        error_detail = (
                            f"Falscher Rückgabetyp: {actual_type.__name__}. "
                            f"Erwartet wurde {expected_type.__name__}"
                        )

        if error_detail is None:
            #   Check values
            return_ok: bool = False
            match expected:
                case float() | np.floating():
                    return_ok = bool(
                        np.isclose(actual, expected, atol=float_atol, rtol=float_rtol)
                    )
                case int() | np.integer():
                    return_ok = actual == expected
                case np.ndarray() if np.issubdtype(expected.dtype, np.floating):
                    return_ok = np.allclose(
                        actual, expected, atol=float_atol, rtol=float_rtol
                    )
                case np.ndarray():
                    return_ok = np.array_equal(actual, expected)
                case np.poly1d():
                    return_ok = TaskRunner.check_result(actual.coeffs, expected.coeffs)[
                        0
                    ]
                case [*elements]:
                    #   Any non-NumPy sequences
                    return_ok = len(actual) == len(elements) and all(
                        TaskRunner.check_result(a, e)[0]
                        for a, e in zip(actual, elements)
                    )

            if not return_ok:
                error_detail = (
                    "Falscher Rückgabewert:\n"
                    + indent(repr(actual), " " * 4)
                    + "\nRichtig wäre:\n"
                    + indent(repr(expected), " " * 4)
                )

        return error_detail is None, error_detail


def panic(msg: str):

    from sys import stderr

    print(msg, file=stderr)
    exit(1)


class TestDriver:
    active = False

    def __init__(self, sheet: Sheet, src_dir: Path):
        self._sheet = sheet
        self._src_dir = src_dir
        self._mp_context = mp.get_context("spawn")

    @staticmethod
    @contextmanager
    def lock():
        if TestDriver.active:
            raise RuntimeError(
                "Die Testsuite wurde mehr als einmal rekursiv aufgerufen!"
            )
        TestDriver.active = True

        try:
            yield None
        finally:
            TestDriver.active = False

    def run_cli(self):
        with TestDriver.lock():
            from argparse import ArgumentParser

            parser = ArgumentParser()
            parser.add_argument("tasks", type=str, nargs="*")
            parser.add_argument("-v", "--verbose", action="store_true")
            args = parser.parse_args()

            selected_subtasks = self._filter_tasks(args.tasks)

            #   Run tasks
            for rep in self._process_subtasks(selected_subtasks):
                print(rep.string(args.verbose), flush=True)

    def run_jupyter(self, tasks: Sequence[int | str]) -> Any:
        with TestDriver.lock():
            from IPython.display import display, Markdown

            tasknames = [str(t) for t in tasks]
            selected_subtasks = self._filter_tasks(tasknames)

            #   Run tasks
            for rep in self._process_subtasks(selected_subtasks):
                # display(Code(rep.markdown(), language="Markdown"))
                display(Markdown(rep.markdown()))

    def _filter_tasks(self, tasknames: Sequence[str]) -> dict[int, set[str]]:
        selected_tasks: set[int] = set()
        selected_subtasks: defaultdict[int, set[str]] = defaultdict(set)

        if tasknames:
            for task_spec in tasknames:
                try:
                    task_id = int(task_spec[0])

                    if len(task_spec) > 1:
                        subtask_id = task_spec[1]
                    else:
                        subtask_id = None

                    selected_tasks.add(task_id)

                    if subtask_id is not None:
                        selected_subtasks[task_id].add(subtask_id)

                except ValueError:
                    panic(f"Ungültige Aufgabe: {task_spec}")
        else:
            selected_tasks = set(t.id for t in self._sheet.tasks)

        for task_id in selected_tasks:
            if task_id > len(self._sheet.tasks):
                panic(f"Ungültige Aufgabe: {task_id}")

        for task_id in selected_tasks:
            if task_id not in selected_subtasks:
                selected_subtasks[task_id] = set(
                    t.id for t in self._sheet.get_task(task_id).subtasks
                )

        for task_id in selected_tasks:
            for subtask_id in selected_subtasks[task_id]:
                if not any(
                    st.id == subtask_id for st in self._sheet.get_task(task_id).subtasks
                ):
                    panic(f"Ungültige Aufgabe: {task_id}{subtask_id}")

        return selected_subtasks

    def _process_subtasks(
        self, selected_subtasks: dict[int, set[str]]
    ) -> Generator[TaskReport, None, None]:
        for task in self._sheet.tasks:
            if task.id in selected_subtasks.keys():
                runner = TaskRunner(task, self._src_dir, self._mp_context)
                if runner.import_and_check():
                    for subtask_id in sorted(selected_subtasks[task.id]):
                        runner.test_subtask(subtask_id)

                runner.report.add_marks()
                yield runner.report
