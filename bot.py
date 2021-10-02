from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2021-10-02',
                     check_out_date='2021-10-10')
    bot.select_adults(count=5)
    print('Exiting page...')