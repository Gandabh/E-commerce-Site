let productListSec = document.getElementById('basket_products');
let innerproductListSec=document.getElementById('basket_info');
let basketbadge=document.getElementById('basketbadge');
let order_detail=document.getElementById('orderdetail');
let total_cost=document.getElementById('totalcost');

let order_detail_checkout=document.getElementById('orderdetail_checkout');
let total_cost_checkout=document.getElementById('totalcost_checkout');
let count=0
let subtotal=0
let total_cost_subtotal=0



 async function ListCarts() {
    count=0
    subtotal=0
    let response = await fetch('http://127.0.0.1:8000/api/cartitems/')
    let productList = await response.json();
    productListSec.innerHTML=``
    innerproductListSec.innerHTML =``
    
    for (let item of productList)
        {
            if (JSON.parse(document.getElementById('user_id').textContent)===item.user){
            subtotal=subtotal+((item.product.price-(item.product.price*item.product.discount)/100)*item.quantity)
            count=count+item.quantity
            productListSec.innerHTML += `<li>
            <div class="media-left">
                <div class="cart-img"> <a href="/product/product-detail/${item.product.id}"> <img class="media-object img-responsive" src="${item.product.cover_image}" alt="..."> </a> </div>
            </div>
            <div class="media-body"><a href="/product/product-detail/${item.product.id}">
                <h6 class="media-heading">${item.product.title}</h6></a>
                <span class="price">${item.product.price-(item.product.price*item.product.discount)/100} USD</span> <span class="qty">QTY: ${item.quantity}</span>
                <span  style="background:${item.color};	
                height: 13px;
                width: 13px;
                display: inline-block;
                border-radius: 50%"></span></div>
            </li>`
        }
    }
  innerproductListSec.innerHTML =`<li>
    <h5 class="text-center">COUNT: ${count} |  SUBTOTAL: ${subtotal} USD</h5>
  </li>`
  basketbadge.innerHTML=`<li><span style="background-color:red"class="badge badge-danger badge-pill">${count}</span><li>`


  return false;
}




let top_rated=document.getElementById('top_rated');

async function TopRateItems() {
  let response = await fetch('http://127.0.0.1:8000/api/products/')
  let productList = await response.json();
  let limit=0
  
  for (let item of productList){  
    if (limit<3){
        
        limit+=1
        top_rated.innerHTML += `<li>
        <div class="media-left">
          <div class="cart-img"> <a href="/product/product-detail/${item.id}"><img class="media-object img-responsive" src="${item.cover_image}" alt="..."> </a> </div>
        </div>
        <div class="media-body">
          <a href="/product/product-detail/${item.id}"><h6 class="media-heading">${item.title}</h6></a>
          <div class="stars"> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> </div>
          <span class="price">${item.price} USD</span> </div>
      </li>`
      }
    }

}







let cartitem = document.getElementById('cartitem');
let cartSubtotal=document.getElementById('cartSubtotal');


async function shoppingcart() {
    total=0
    subtotal=0
    lastsubtotal=0
    let response = await fetch('http://127.0.0.1:8000/api/cartitems/')
    let productList = await response.json();
    cartitem.innerHTML=``

    for (let item of productList)
        {
            if (JSON.parse(document.getElementById('user_id').textContent)===item.user){
            total=(item.product.price-(item.product.price*item.product.discount)/100)
            subtotal=((item.product.price-(item.product.price*item.product.discount)/100)*item.quantity)
            total_cost_subtotal=total_cost_subtotal+subtotal

            var length = 20;
            var myString = item.product.description;
            var myTruncatedString = myString.substring(0,length);

            cartitem.innerHTML += `<ul class="row cart-details">
            <li class="col-sm-6">
              <div class="media"> 
                <!-- Media Image -->
                <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${item.product.cover_image}" alt=""> </a> </div>
                
                <!-- Item Name -->
                <div class="media-body">
                  <div class="position-center-center">
                  <a href="/product/product-detail/${item.product.id}"><h5>${item.product.title}</h5></a>
                    <p>${myTruncatedString}</p>

                  <a style="background:${item.color};	
                  height: 13px;
                  width: 13px;
                  display: inline-block;"></a>
                  </div>
                </div>
              </div>
            </li>
            
            <!-- PRICE -->
            <li class="col-sm-2">
              <div class="position-center-center"> <span class="price"><small>$</small>${total} </span> </div>
            </li>
            
            <!-- QTY -->
            <li class="col-sm-1">
              <div class="position-center-center">
                <div class="quinty"> 
                  <!-- QTY -->
                  <div class="position-center-center"> <span class="price">${item.quantity}  </span> </div>
                </div>
              </div>
            </li>


            <!-- TOTAL PRICE -->
            <li class="col-sm-2">
              <div class="position-center-center"> <span class="price"><small>$</small>${subtotal} </span> </div>
            </li>
            
            <!-- REMOVE -->
            <li class="col-sm-1">
              <div class="position-center-center"><button style="border:none; background-color:white;" id="basket-delete" onclick="deleteItem(event, ${item.id}); return false;"><i class="icon-close"></i></button> </div>
              

             
            </li>
          </ul>`


          order_detail.innerHTML+=`<p>${item.product.title}<span><small>$</small>${subtotal} </span></p>`
          total_cost.innerHTML=`<p class="all-total">TOTAL COST<span><small>$</small>${total_cost_subtotal} </span></p></div>`


        }
      
    }

  

  
}






async function Checkout() {
  total=0
  subtotal=0
  lastsubtotal=0
  let response = await fetch('http://127.0.0.1:8000/api/cartitems/')
  let productList = await response.json();
  for (let item of productList)
      {
          if (JSON.parse(document.getElementById('user_id').textContent)===item.user){
          total=(item.product.price-(item.product.price*item.product.discount)/100)
          subtotal=((item.product.price-(item.product.price*item.product.discount)/100)*item.quantity)
          total_cost_subtotal=total_cost_subtotal+subtotal


        order_detail_checkout.innerHTML+=`<p>${item.product.title}<span><small>$</small>${subtotal} </span></p>`
        total_cost_checkout.innerHTML=`<p class="all-total">TOTAL COST<span><small>$</small>${total_cost_subtotal} </span></p></div>`

      }
    
  }
}








let Wishlistitem = document.getElementById('Wishlistitem');

async function Wishlist() {
    let response = await fetch('http://127.0.0.1:8000/api/likeditems/')
    let productList = await response.json();
    Wishlistitem.innerHTML=``

    for (let item of productList)
        {
            if (JSON.parse(document.getElementById('user_id').textContent)===item.user){
            total=(item.product.price-(item.product.price*item.product.discount)/100)


            var length = 20;
            var myString = item.product.description;
            var myTruncatedString = myString.substring(0,length);

            Wishlistitem.innerHTML += `<ul class="row cart-details">
            <li class="col-sm-6">
              <div class="media"> 
                <!-- Media Image -->
                <div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${item.product.cover_image}" alt=""> </a> </div>
                
                <!-- Item Name -->
                <div class="media-body">
                  <div class="position-center-center">
                  <a href="/product/product-detail/${item.product.id}"><h5>${item.product.title}</h5></a>
                    <p>${myTruncatedString}</p>
                  </div>
                </div>
              </div>
            </li>
            
            <!-- PRICE -->
            <li class="col-sm-2">
              <div class="position-center-center"> <span class="price"><small>$</small>${total} </span> </div>
            </li>


            <!-- REMOVE -->
            <li class="col-sm-1">
            <div class="position-center-center"><button style="border:none; background-color:white;" id="basket-delete" onclick="disLikeItem(${item.id}); return false;"><i class="icon-close"></i></button> </div>
              

          </ul>`


 


        }
      
    }

  

  
}
window.onload = () => {
    TopRateItems();
    ListCarts();
    shoppingcart();
    Checkout() ;
    Wishlist()
    
}






