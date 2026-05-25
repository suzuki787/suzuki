// Savdo avtomati mantig'i
const VendingMachine = {
    balance: 0,
    
    addMoney: function(amount) {
        this.balance += amount;
        console.log("Balans yangilandi: " + this.balance);
    },

    buyCar: function(price) {
        if (this.balance >= price) {
            this.balance -= price;
            return true;
        }
        return false;
    }
};
