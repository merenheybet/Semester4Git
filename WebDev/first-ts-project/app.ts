const button = document.getElementById('increment') as HTMLButtonElement;
const countDisplay = document.getElementById('count') as HTMLParagraphElement;
const resetButton = document.getElementById('reset') as HTMLButtonElement
const imageContainer = document.getElementById('image-container') as HTMLDivElement

let count: number = 0;
let prank_triggered: boolean = false

async function getMeme(){
    const url = "https://api.imgflip.com/get_memes";
    try{
        const raw_response = await fetch(url);
        if(!raw_response.ok){
            throw new Error(`Response Status: ${raw_response.status}`);
        }

        const response = await raw_response.json();
        //console.log(response);
        if(!response.success){
            throw new Error("API not responding...");
        }
        response.data.memes


    }
    catch(error){
        console.error(error);
    }
}

function toggle_prank(increment: boolean){
    imageContainer.innerHTML = '';
    if(!prank_triggered&&!increment){
        count = 0;
        countDisplay.textContent = "Haha, you hovered over the reset button";

        const image = document.createElement('img');

        image.src = 'el-risitas-juan-joya-borja.png';
        image.alt = 'Reset image';
        imageContainer.appendChild(image);
        prank_triggered = true;
    }

    else{
        countDisplay.textContent = "";
        prank_triggered = false;
    }
        
}

button.addEventListener('click', () => {
    getMeme();
    //toggle_prank(true);
    //count++;
    //countDisplay.textContent = "You've clicked " + count.toString() + " times";
});

resetButton.addEventListener('mouseenter', () => {
    toggle_prank(false);
});

resetButton.addEventListener('mouseleave', () => {
    toggle_prank(true);
});