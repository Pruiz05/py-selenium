from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.change_language(language='en-us')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2021-10-02',
                     check_out_date='2021-10-10')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filtration()
    print('Exiting page...')