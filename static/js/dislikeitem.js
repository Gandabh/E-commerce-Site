
async  function disLikeItem(id){
    location.reload();
    wishlist_item=id


   let res = await fetch('http://127.0.0.1:8000/api/likeditems/'+ wishlist_item, {
            method: 'DELETE',
            headers:{
                'Content-Type': 'application/json',
                "X-CSRFToken": form.csrfmiddlewaretoken.value
            },
        });
    



    };

 
  
   

   