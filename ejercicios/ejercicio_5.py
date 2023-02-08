if __name__=="__main__":
    farenheit=float(input("\nDigite los grados Farenheit a convertir: "))
    def farenheit_to_celcius(f):
        celcius=(f-32)*(5/9)
        return celcius

    print(f"\n{farenheit}°F son equivalentes a {farenheit_to_celcius(farenheit)}°C")