"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const question_div = document.getElementById("question");
const choices_div = document.getElementById("choices");
const next_button = document.getElementById("next");
let questions = [];
let question_answered = false;
function getQuestions() {
    return __awaiter(this, void 0, void 0, function* () {
        const response = yield fetch("questions.json");
        if (!response.ok) {
            throw new Error(`Error status: ${response.status}`);
        }
        questions = yield response.json();
        return questions;
    });
}
/**
 * Displays the question from the source JSON File with the given index
 * @param index index of the Question to be displayed
 */
function displayQuestion(index) {
    return __awaiter(this, void 0, void 0, function* () {
        next_button.disabled = true;
        question_answered = false;
        if (questions.length == 0) {
            yield getQuestions();
        }
        const current_question = questions[index];
        question_div.innerHTML = '';
        const question_html = document.createElement('p');
        question_html.innerHTML = current_question.question;
        console.log(current_question.question);
        question_div.appendChild(question_html);
        return displayChoicesForQuestion(current_question);
    });
}
function displayChoicesForQuestion(current_question) {
    choices_div.innerHTML = "";
    let option_buttons = [];
    current_question.choices.forEach((choice_iter, choice_index) => {
        const choice_button = document.createElement('button');
        option_buttons[choice_index] = choice_button;
        choice_button.textContent = choice_iter;
        choice_button.setAttribute('class', 'choice-btn');
        choice_button.addEventListener('click', () => handleClick(choice_button, choice_index, current_question.correctAnswer, option_buttons));
        choices_div.appendChild(choice_button);
    });
}
function handleClick(button, index, correct_answer, buttons) {
    if (index === correct_answer) {
        button.setAttribute('id', 'correct');
        buttons.forEach((butIter) => {
            if (butIter === button) { }
            else {
                butIter.disabled = true;
            }
        });
        next_button.disabled = false;
    }
    else {
        button.setAttribute('id', 'wrong');
    }
}
next_button.addEventListener('click', () => __awaiter(void 0, void 0, void 0, function* () {
    question_answered = true;
    current_question_number++;
    if (current_question_number >= questions.length) {
        console.log("Game finished");
    }
    else {
        yield displayQuestion(current_question_number);
    }
}));
let current_question_number = 0;
displayQuestion(current_question_number);
