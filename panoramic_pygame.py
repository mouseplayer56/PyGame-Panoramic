import pygame as pg
import os

pg.init()
width, height = 1280, 720
bg = pg.display.set_mode((width, height))
pg.display.set_caption("Panorama")
fps = 60

exit_code_normal = 0
exit_code_not_normal = -1
exit_code_positive = 1

panorama_x, panorama_x_local = 0, 0
pgp = 0
g_t = -1
pretype = ""
lookspeed = 3000
determiner = False
typing = False
ds = True

panorama_list = ["1N", "2E", "3S", "4W"]  # r=0, 1, 2, 3 (RIGHT)// r=0, -1, -2, -3 (LEFT)
panorama_list_extra = [["LEFTMOST", "dimensions"], ["MIDDLE", "dimensions"], ["RIGHTMOST", "dimensions"]]  # will be modified once the program loads,
# ple[x][0] will show values in panorama_list, and ple[x][1] will show values where the screen is.


def pg_clock(curtick, maxtick):  # clock based on frames gone by (as determined by the game's while loop)
    # -1 is default/starting value. it should be, anyway.
    curtick += 1
    if curtick >= maxtick:
        curtick = -1
        return curtick, True
    else:
        return curtick, False


while ds:  # basically lets the GUI part of this run.

    bg.fill((125, 30, 60))

    for e in pg.event.get():  # basic quit mechanic
        if e.type == pg.QUIT:
            pg.quit()
            exit(f"exit code {exit_code_normal} -- pygame.QUIT event called (by user).")

    if pg.key.get_pressed()[pg.K_a]:  # if A is pressed, move left.
        panorama_x = int(panorama_x + (lookspeed * pgp // 1))
        if panorama_x > 5120:
            panorama_x -= 5120

    if pg.key.get_pressed()[pg.K_d]:  # if D is pressed, move right
        panorama_x = int(panorama_x - (lookspeed * pgp // 1))
        if panorama_x < -5120:
            panorama_x += 5120

    r = (panorama_x // 1280) * -1  # r determines what panel in panorama_list is loaded
    if r > 0:
        r -= 1
    # low and hi represent the right & left panels to be loaded.
    low = r - 1
    hi = r + 1

    panorama_x_local = panorama_x + (r * 1280)  # positioning of the panel relative to itself (using r)

    try:
        panorama_list[low]
        panorama_list[hi]
        # if either of these are too high/low, it will flag up an error. Hence, rolls over to the except clause.
    except:
        if low < 0:
            low = len(panorama_list)
            # load from top
            pass
        if hi > len(panorama_list) - 1:
            hi = 0
            # load from bottom
            pass
    finally:
        # simplifies variables for multi-use. This takes up more memory, but it makes it easier to read the code.
        p_right, p_mid, p_left = panorama_list[low], panorama_list[r], panorama_list[hi]
        pd_right, pd_mid, pd_left = panorama_x_local - 1280, panorama_x_local, panorama_x_local + 1280

        # adds the variables into ple, so they can actually be used.
        panorama_list_extra[0] = p_right, pd_right
        panorama_list_extra[1] = p_mid, pd_mid
        panorama_list_extra[2] = p_left, pd_left

        # loads respective screens to the left & right of the player
        bg.blit(pg.transform.scale(pg.image.load(
            os.path.join('assets', f'{p_mid}.bmp')),
            (1280, 720)),
            (pd_mid, 0))
        bg.blit(pg.transform.scale(pg.image.load(
            os.path.join('assets', f'{p_right}.bmp')),
            (1280, 720)),
            (pd_right, 0))
        bg.blit(pg.transform.scale(pg.image.load(
            os.path.join('assets', f'{p_left}.bmp')),
            (1280, 720)),
            (pd_left, 0))

    # here's the fun part -- adding stickmen & other stuff into the mix, and allowing them to be viewed from any angle (as long as the respective space is loaded).
    for panora_part in panorama_list_extra:
        if panora_part[0] == "1N":
            bg.blit(pg.transform.scale(pg.image.load(
                os.path.join('assets', 'panorama.bmp')),
                (200, 200)),
                (panora_part[1] + 500, 50))

    print(f"{r}, {panorama_x}, {panorama_x_local} -- {panorama_list_extra}")

    pg.display.flip()
    pgp = pg.time.Clock().tick(fps) / 1000
