
async  function LikeItem(id){
    let heart=document.getElementById('likeItem'+id)
    const user_id = JSON.parse(document.getElementById('user_id').textContent);

    let flag=0
    let basketID=0
    let basket = await fetch('http://127.0.0.1:8000/api/likeditems/')
    let productList = await basket.json();
    for (let item of productList){
        if (item.product.id==id & JSON.parse(document.getElementById('user_id').textContent)===item.user){
            flag=1
            wishlist_item=item.id
        }
    }

    if (flag==1){
        heart.style.color = "gray";

        let res = await fetch('http://127.0.0.1:8000/api/likeditems/'+ wishlist_item, {
            method: 'DELETE',
            headers:{
                'Content-Type': 'application/json',
                "X-CSRFToken": form.csrfmiddlewaretoken.value
            },
        });
    
        alert('Product deleted from Wishlist')
        return false;


    }else{
    heart.style.color = "red";

    let postData = {
        'user': user_id,
        'product': id,

    }

    let res = await fetch('http://127.0.0.1:8000/api/likeditems/', {
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
        alert('Product added to Wishlist');
    }else{
        heart.style.color = "gray";
        alert('Something is wrong, Sign in to add to your Wishlist');
    }



}

}


 
  
   

   