document.getElementById('basket-adder')
.addEventListener('submit', async  function(e){
    e.preventDefault();
    const user_id = JSON.parse(document.getElementById('user_id').textContent);
    let flag=0
    let basketID=0
    let basket = await fetch('http://127.0.0.1:8000/api/cartitems/')
    let productList = await basket.json();
    for (let item of productList){
        if (item.product.id==getID() & JSON.parse(document.getElementById('user_id').textContent)===item.user & item.color==this.color.value){
            flag=1
            basketID=item.id 
            basketCount=item.quantity
        }
    }

    if (flag==1){

        let postData = {
            'quantity':parseInt(this.qty.value) + parseInt(basketCount),
        }

        let res = await fetch('http://127.0.0.1:8000/api/cartitems/'+basketID + '/', {
            method: 'PATCH',
            headers:{
                'Content-Type': 'application/json',
                "X-CSRFToken": form.csrfmiddlewaretoken.value
            },
            body: JSON.stringify(postData)
        });
        if (res.ok){
            let post = await res.json()
            ListCarts(post);
            alert('Product added to Basket');
        }else{
            alert('Something is wrong, Sign in to add to your card');
        }
    }else{

    console.log("user", user_id)
    console.log("product",getID())
    console.log(this.color.value)

    let postData = {
        'user': user_id,
        'product': getID(),
        'quantity':this.qty.value,
        'color': this.color.value,


    }

    let res = await fetch('http://127.0.0.1:8000/api/cartitems/', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            "X-CSRFToken": form.csrfmiddlewaretoken.value
        },
        body: JSON.stringify(postData)
    });
    if (res.ok){
        let post = await res.json()
        ListCarts(post);
        alert('Product added to Basket');
    }else{
        alert('Something is wrong, Sign in to add to your card');
    }



}

})



function getID(){
    var url =window.location.href;
    var id = url.split("/")[6];
    console.log(id)
    return id
   }
