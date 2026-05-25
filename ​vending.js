/* vending.js */
const VendingMachine = {
    balance: 0,
    addMoney: function(amount) {
        this.balance += amount;
        console.log("Balans yangilandi: " + this.balance + "$");
    },
    buyCar: function(price) {
        if (this.balance >= price) {
            this.balance -= price;
            return { success: true, message: "Tabriklaymiz, xarid muvaffaqiyatli!" };
        }
        return { success: false, message: "Balans yetarli emas!" };
    }
};
