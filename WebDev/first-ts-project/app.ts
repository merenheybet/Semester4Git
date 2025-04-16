const button = document.getElementById('increment') as HTMLButtonElement;
const countDisplay = document.getElementById('count') as HTMLParagraphElement;
const resetButton = document.getElementById('reset') as HTMLButtonElement
const imageContainer = document.getElementById('image-container') as HTMLDivElement

let count: number = 0;
let prank_triggered: boolean = false

async function getMeme(): Promise<string> {
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

        const memes = response.data.memes;
        let randIndex: number = Math.floor(Math.random() * response.data.memes.length);
        const memeURL: string = memes[randIndex].url;

        return memeURL || "";

    }
    catch(error){
        console.error(error);
        return "";
    }
}

async function toggle_prank(increment: boolean){
    imageContainer.innerHTML = '';
    if(!prank_triggered&&!increment){
        count = 0;
        countDisplay.textContent = "Haha, you hovered over the reset button";

        const image = document.createElement('img');

        image.src = await getMeme();
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