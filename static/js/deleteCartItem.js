async  function deleteItem(e,id){
    e.preventDefault();
    location.reload();
    let res = await fetch('http://127.0.0.1:8000/api/cartitems/'+id, {

        method: 'DELETE',
        headers:{
            'Content-Type': 'application/json',
            "X-CSRFToken": form.csrfmiddlewaretoken.value
        },
    });

    alert('Product removed from Cart')
    return false;
}
