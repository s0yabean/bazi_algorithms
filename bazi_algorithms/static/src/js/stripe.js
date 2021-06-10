console.log("Should Load Automatically - Click Shift Command R to refresh!");

//Get Stripe publishable key
//client calls this to server whenver payment page is loaded, since this script runs automatically
fetch("/stripe_public")
.then((result) => { return result.json(); })
.then((data) => {
  const stripe = Stripe(data.publicKey);
  console.log(data.publicKey);

  window.onload=function(){

  document.querySelector("#plusPlanSubmitBtn").addEventListener("click", () => {
    console.log("Clicked Plus Plan");
    fetch("/create-checkout-session/plusplan")
    .then((result) => { return result.json(); })
    .then((data) => {
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });

  document.querySelector("#premiumPlanSubmitBtn").addEventListener("click", () => {
    console.log("Clicked Premium Plan");
    fetch("/create-checkout-session/premiumplan")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });

  document.querySelector("#annualPlanSubmitBtn").addEventListener("click", () => {
    console.log("Clicked Annual Plan");
    fetch("/create-checkout-session/annualplan")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
}
});

