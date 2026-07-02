class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`
    def to_usd(amount: float, currency_code: str) -> float:
        if currency_code in CurrencyConverter.rates:
            return amount * CurrencyConverter.rates[currency_code]
        else:
            raise ValueError(f"Currency code '{currency_code}' not supported.")
        
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
