import os

from PIL import Image, ImageTk

import static_vars

WIDTH, HEIGHT = 650, 300

MAIN = "Negotiator.jpg"

airport = "Airport.jpg"
defence_academy = 'Defence_academy.jpg'
bandit_den = 'Bandit_den.jpg'
train_station = 'Train_Station.jpg'
industrial_zone = 'Industrial_zone.jpg'
prison_facility = 'Prisons.jpg'
city_center = 'City_center.jpg'
central_market = 'Market.jpg'
bureau_dechange = 'BDC.jpg'
hospital = 'Hospital.jpg'
central_mosque = 'Mosque.jpg'
black_market = 'Black_market.jpg'
check_point = 'Checkpoint.jpg'
bandit_hideout = 'Bandit_hideout.jpg'
exchange_point = 'Exchange_point.jpg'


photo_cache = {}


def get_photo_image(file_name):
    if file_name in photo_cache:
        return photo_cache.get(file_name)

    path = "images" + os.sep + file_name
    if os.path.exists(path):
        img = ImageTk.PhotoImage(Image.open(path).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        photo_cache[file_name] = img
        return img

    return None


def reset_photo(photo):
    static_vars.photo_label.config(image='')
    if photo is None:
        return
    p_image = get_photo_image(photo)
    if p_image is not None:
        static_vars.photo_label.configure(image=p_image)

    # def DrainHealth(self):
    #     """ Negotiator loosing all health and dies"""
    #     self.health -= 5
    #     if self.health == 0:
    #         return f'Game Over {quit()}'