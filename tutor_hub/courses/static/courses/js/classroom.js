const buttonToggled = document.querySelector('.button-nav');
const buttonClass = document.querySelector('.addClass');
const dropdown =  document.querySelector('.drop-downmenu');
const targetClass = document.querySelector('.addClass');
buttonToggled.addEventListener('click',()=>{ 
    document.querySelector('.btnOpen').classList.toggle('active');
    document.querySelector('body').classList.toggle('removeScroll');
});
buttonClass.addEventListener('click',()=>{
    document.querySelector('.drop-downmenu').classList.toggle('openmenu');
})

window.addEventListener('click',(event)=>{
    if(!(event.target===targetClass)){
        dropdown.classList.remove('openmenu');
    } 
})