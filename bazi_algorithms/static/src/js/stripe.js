console.log("Sanity check! Click Shift Command R to refresh!");

//Get Stripe publishable key
//client calls this to server whenver payment page is loaded, since this script runs automatically
fetch("/stripe_public")
.then((result) => { return result.json(); })
.then((data) => {
  const stripe = Stripe(data.publicKey);

  // Can try convert to a post request to get the correct package type for the line_items
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    console.log("clicked");
    fetch("/create-checkout-session")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});