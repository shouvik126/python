
while True:
    try:
        tuna=int(input('Enter your fav no:='))
        print(18/tuna)
        break
    except ValueError:
        print('Make sure and enter a number')
    except ZeroDivisionError:
        print('input zero')
    except:
        break
    finally:
        print('Thank u')


