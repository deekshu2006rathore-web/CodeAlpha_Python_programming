import csv

# Hardcoded dictionary defining stock prices
STOCK_PRICES = {
    "AAPL": 230.50,
    "MSFT": 425.20,
    "GOOGL": 178.90,
    "AMZN": 184.40,
    "NVDA": 125.60,
    "TSLA": 195.30
}

def save_to_txt(portfolio, total_investment):
    """Handles TXT file generation"""
    with open("portfolio_summary.txt", "w") as txt_file:
        txt_file.write("--- STOCK PORTFOLIO SUMMARY ---\n\n")
        txt_file.write(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Total':<10}\n")
        txt_file.write("-" * 40 + "\n")
        for item in portfolio:
            txt_file.write(f"{item['ticker']:<10}{item['quantity']:<10}${item['price']:<9.2f}${item['total']:<9.2f}\n")
        txt_file.write("-" * 40 + "\n")
        txt_file.write(f"TOTAL INVESTMENT VALUE: ${total_investment:.2f}\n")
    print("💾 Success! Text report saved as 'portfolio_summary.txt'")

def save_to_csv(portfolio, total_investment):
    """Handles CSV file generation"""
    with open("portfolio_summary.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Ticker", "Quantity", "Price Per Share", "Total Value"])
        for item in portfolio:
            writer.writerow([item['ticker'], item['quantity'], f"{item['price']:.2f}", f"{item['total']:.2f}"])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", f"{total_investment:.2f}"])
    print("💾 Success! CSV data spreadsheet saved as 'portfolio_summary.csv'")

def run_stock_tracker():
    print("--- SIMPLE STOCK TRACKER ---")
    print("Available stock tickers in system:", ", ".join(STOCK_PRICES.keys()))
    
    portfolio = []
    total_investment = 0.0
    
    # 1. Input/Output Loop to gather user stock details
    while True:
        ticker = input("\nEnter stock ticker (or type 'done' to calculate): ").strip().upper()
        if ticker == "DONE":
            break
            
        if ticker not in STOCK_PRICES:
            print(f"⚠️ '{ticker}' is not in our system database. Please try a valid ticker.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {ticker}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than zero.")
                continue
        except ValueError:
            print("❌ Invalid number. Please enter a valid integer.")
            continue
            
        # 2. Calculations
        price = STOCK_PRICES[ticker]
        position_value = quantity * price
        total_investment += position_value
        
        portfolio.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "total": position_value
        })
        print(f"✅ Added {quantity} shares of {ticker} (${price:.2f} each).")

    if not portfolio:
        print("\nNo stocks added. Exiting portfolio tracker.")
        return

    # 3. Display Result Summary
    print("\n======================================")
    print("      FINAL PORTFOLIO SUMMARY         ")
    print("======================================")
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Total':<10}")
    print("-" * 40)
    for item in portfolio:
        print(f"{item['ticker']:<10}{item['quantity']:<10}${item['price']:<9.2f}${item['total']:<9.2f}")
    print("-" * 40)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:.2f}")
    print("======================================")

    # 4. Interactive Download Menu Options
    while True:
        print("\n--- DOWNLOAD OPTIONS MENU ---")
        print("1. Download as Text File (.txt)")
        print("2. Download as Excel/CSV File (.csv)")
        print("3. Download BOTH formats (.txt & .csv)")
        print("4. Exit without downloading")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            save_to_txt(portfolio, total_investment)
            break
        elif choice == "2":
            save_to_csv(portfolio, total_investment)
            break
        elif choice == "3":
            save_to_txt(portfolio, total_investment)
            save_to_csv(portfolio, total_investment)
            break
        elif choice == "4":
            print("Exiting tracker. Data was not saved locally.")
            break
        else:
            print("❌ Invalid option selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    run_stock_tracker()
