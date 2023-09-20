// Initialize an empty cart array
    let cart = [];

    // Function to add a product to the cart
    function addToCart(productName, productPrice) {
        const product = {
            name: productName,
            price: productPrice,
        };
        cart.push(product);
        alert(`${productName} added to cart.`);
    }

    // Function to calculate the total price of items in the cart
    function calculateTotalPrice() {
        let total = 0;
        for (const product of cart) {
            total += product.price;
        }
        return total;
    }

    // Function to display the cart and checkout total
    function checkout(productName, productPrice) {
        addToCart(productName, productPrice);
        const total = calculateTotalPrice();
        alert(`Cart Contents:\n\n${cart.map((item) => `${item.name}: $${item.price.toFixed(2)}`).join('\n')}\n\nTotal: $${total.toFixed(2)}`);
    }