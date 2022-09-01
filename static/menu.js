let menu=document.getElementById('sreyas')

menu.addEventListener("click",function(){
    console.log('button is clicked')

    document.getElementById('navbar').style.width="100%"

})
let close=document.getElementById('menuclose')

close.addEventListener("click",function(){
    console.log('close is clicked')

    document.getElementById('navbar').style.width="0%"
})
