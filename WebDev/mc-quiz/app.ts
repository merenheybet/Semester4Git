type Question = {
    id: number;
    question: string;
    choices: string[];
    correctAnswer: number; // index of the correct choice
}

const question_div = document.getElementById("question") as HTMLDivElement
const choices_div = document.getElementById("choices") as HTMLDivElement
const next_button = document.getElementById("next") as HTMLButtonElement

let questions: Question[] = [];
let question_answered: boolean = false;

async function getQuestions(){
    const response = await fetch("questions.json")
    if(!response.ok){
        throw new Error(`Error status: ${response.status}`);
    }

    questions = await response.json();
    return questions;
}

/**
 * Displays the question from the source JSON File with the given index
 * @param index index of the Question to be displayed
 */

async function displayQuestion(index: number){
    next_button.disabled = true;
    question_answered = false;
    if(questions.length == 0){
        await getQuestions();
    }
    const current_question = questions[index];

    question_div.innerHTML = '';
    const question_html = document.createElement('p');
    question_html.innerHTML = current_question.question;
    console.log(current_question.question);

    question_div.appendChild(question_html);

    return displayChoicesForQuestion(current_question);
}


function displayChoicesForQuestion(current_question: Question) {
    choices_div.innerHTML = "";
    let option_buttons: HTMLButtonElement[] = [];

    current_question.choices.forEach((choice_iter, choice_index) => {
        const choice_button = document.createElement('button');
        option_buttons[choice_index] = choice_button;
        choice_button.textContent = choice_iter;
        choice_button.setAttribute('class', 'choice-btn');
        choice_button.addEventListener('click', () => handleClick(choice_button, choice_index, current_question.correctAnswer, option_buttons));
        choices_div.appendChild(choice_button);
    });
}

function handleClick(button:HTMLButtonElement, index: number, correct_answer: number, buttons: HTMLButtonElement[]): any {
    if (index === correct_answer){
        button.setAttribute('id', 'correct');
        buttons.forEach((butIter) => {
            if(butIter === button){}
            else{butIter.disabled = true;}
        });
        next_button.disabled = false;
    }
    else{
        button.setAttribute('id', 'wrong');
    }
}

next_button.addEventListener('click', async () => {
    question_answered = true;
    current_question_number++;
    if(current_question_number >= questions.length){
        console.log("Game finished");
    }
    else{
        await displayQuestion(current_question_number);
    }
});

let current_question_number = 0;
displayQuestion(current_question_number);