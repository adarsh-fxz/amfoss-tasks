var crash = new Audio("./sounds/crash.mp3");
var kick = new Audio("./sounds/kick-bass.mp3");
var snare = new Audio("./sounds/snare.mp3");
var tom1 = new Audio("./sounds/tom-1.mp3");
var tom2 = new Audio("./sounds/tom-2.mp3");
var tom3 = new Audio("./sounds/tom-3.mp3");
var tom4 = new Audio("./sounds/tom-4.mp3");

const buttons = document.querySelectorAll(".drum");
buttons.forEach((button) => {
    button.addEventListener("click", function () {
        const buttonInnerHTML = this.innerHTML;
        sound(buttonInnerHTML);
        animation(buttonInnerHTML);
    });
});

document.addEventListener("keypress", function (event) {
    sound(event.key);
    animation(event.key);
});

function sound(key) {

    switch (key) {
        case "w":
            crash.load()
            crash.play();
            break;

        case "a":
            kick.load()
            kick.play();
            break;

        case "s":
            snare.load()
            snare.play();
            break;

        case "d":
            tom1.load()
            tom1.play();
            break;

        case "j":
            tom2.load()
            tom2.play();
            break;

        case "k":
            tom3.load()
            tom3.play();
            break;

        case "l":
            tom4.load()
            tom4.play();
            break;

        default:
            console.log("Invalid key/button pressed");
    };
};

function animation(currentKey) {
    var activeButton = document.querySelector("." + currentKey);

    activeButton.classList.add("animation");

    setTimeout(function () {
        activeButton.classList.remove("animation");
    }, 100);
};