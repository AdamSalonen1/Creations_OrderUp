function submit(){
    let num = document.getElementById('number').value
    document.getElementById('test').value = num
    document.getElementById('number').value=''

    $.ajax({
        url: "employee/",
        method: "POST",
        data: {'number' : document.getElementById('number').value}
    })
}