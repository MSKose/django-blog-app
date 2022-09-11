let element = document.querySelector('.alert-this');

console.log(element)
setTimeout(function () {
    element.style.display = 'none';
    console.log("------")
    console.log(`${element.style.display}`)
    console.log("------")
}, 3000);

document.body.addEventListener('htmx:configRequest', (e) => {
    e.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
})
    
