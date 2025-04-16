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
const button = document.getElementById('increment');
const countDisplay = document.getElementById('count');
const resetButton = document.getElementById('reset');
const imageContainer = document.getElementById('image-container');
let count = 0;
let prank_triggered = false;
function getMeme() {
    return __awaiter(this, void 0, void 0, function* () {
        const url = "https://api.imgflip.com/get_memes";
        try {
            const raw_response = yield fetch(url);
            if (!raw_response.ok) {
                throw new Error(`Response Status: ${raw_response.status}`);
            }
            const response = yield raw_response.json();
            //console.log(response);
            if (!response.success) {
                throw new Error("API not responding...");
            }
            const memes = response.data.memes;
            let randIndex = Math.floor(Math.random() * response.data.memes.length);
            const memeURL = memes[randIndex].url;
            return memeURL || "";
        }
        catch (error) {
            console.error(error);
            return "";
        }
    });
}
function toggle_prank(increment) {
    return __awaiter(this, void 0, void 0, function* () {
        imageContainer.innerHTML = '';
        if (!prank_triggered && !increment) {
            count = 0;
            countDisplay.textContent = "Haha, you hovered over the reset button";
            const image = document.createElement('img');
            image.src = yield getMeme();
            image.alt = 'Reset image';
            imageContainer.appendChild(image);
            prank_triggered = true;
        }
        else {
            countDisplay.textContent = "";
            prank_triggered = false;
        }
    });
}
button.addEventListener('click', () => {
    toggle_prank(true);
    count++;
    countDisplay.textContent = "You've clicked " + count.toString() + " times";
});
resetButton.addEventListener('mouseenter', () => {
    toggle_prank(false);
});
resetButton.addEventListener('mouseleave', () => {
    toggle_prank(true);
});
