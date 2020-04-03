
class Object_settings:
    # The sun settings:
    sun_color = (255, 255, 0)
    sun_radius = 70
    sun_X = int(2500 / 2)
    sun_Y = int(1200 / 2)

    # Mercury settings
    mercury_color = (110, 110, 110)
    mercury_radius = int(sun_radius / 285)
    mercury_X = sun_X + 100
    mercury_Y = sun_Y
    mercury_speed = 1

    # Venus settings
    venus_color = (171, 97, 23)
    venus_radius = int(sun_radius / 119)
    venus_X = sun_X + 250
    venus_Y = sun_Y
    venus_speed = mercury_speed / 1.37

    # Earth settings
    earth_color = (65, 105, 225)
    earth_radius = int(sun_radius / 109)
    earth_Y = sun_Y
    earth_X = sun_X + 350
    earth_speed = mercury_speed / 1.60

    # Mars settings
    mars_color = (255, 0, 0)
    mars_radius = int(sun_radius / 200)
    mars_Y = sun_Y
    mars_X = sun_X + 500
    mars_speed = mercury_speed / 1.98

    # Jupiter settings
    jupiter_color = (216, 202, 157)
    jupiter_radius = int(sun_radius / 10)
    jupiter_Y = sun_Y
    jupiter_X = sun_X + 650
    jupiter_speed = mercury_speed / 3.66

    # Saturn settings
    saturn_color = (220, 188, 120)
    saturn_radius = int(sun_radius / 12)
    saturn_X = sun_X + 800
    saturn_Y = sun_Y
    saturn_speed = mercury_speed / 4.94

    # Uranus settings
    uranus_color = (202, 240, 243)
    uranus_radius = int(sun_radius / 27.5)
    uranus_Y = sun_Y
    uranus_X = sun_X + 950
    uranus_speed = mercury_speed / 7.03

    # Neptune settings
    neptune_color = (96, 151, 244)
    neptune_radius = int(sun_radius / 28.2)
    neptune_Y = sun_Y
    neptune_X = sun_X + 1100
    neptune_speed = mercury_speed / 8.81

    # Satellite
    satellite_color = (255, 255, 255)
