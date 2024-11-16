import pygame as pg
import os

pg.init()
width, height = 1280, 720
bg = pg.display.set_mode((width, height))
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
panorama_list_extra = [["LEFTMOST", "dimensions"], ["MIDDLE", "dimensions"], ["RIGHTMOST", "dimensions"]]


def pg_clock(curtick, maxtick):  # clock based on frames gone by (as determined by the game's while loop)
    # -1 is default/starting value. it should be, anyway.
    curtick += 1
    if curtick >= maxtick:
        curtick = -1
        return curtick, True
    else:
        return curtick, False


while ds:

    bg.fill((125, 30, 60))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit(f"exit code {exit_code_normal} -- pygame.QUIT event called (by user).")

    if pg.key.get_pressed()[pg.K_a]:
        panorama_x = int(panorama_x + (lookspeed * pgp // 1))
        if panorama_x > 5120:
            panorama_x -= 5120

    if pg.key.get_pressed()[pg.K_d]:
        panorama_x = int(panorama_x - (lookspeed * pgp // 1))
        if panorama_x < -5120:
            panorama_x += 5120

    r = (panorama_x // 1280) * -1
    if r > 0:
        r -= 1
    low = r - 1
    hi = r + 1

    panorama_x_local = panorama_x + (r * 1280)

    try:
        panorama_list[low]
        panorama_list[hi]
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
        p_right, p_mid, p_left = panorama_list[low], panorama_list[r], panorama_list[hi]
        pd_right, pd_mid, pd_left = panorama_x_local - 1280, panorama_x_local, panorama_x_local + 1280
        panorama_list_extra[0] = p_right, pd_right
        panorama_list_extra[1] = p_mid, pd_mid
        panorama_list_extra[2] = p_left, pd_left

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

    for greenfn in panorama_list_extra:
        if greenfn[0] == "1N":
            bg.blit(pg.transform.scale(pg.image.load(
                os.path.join('assets', 'panorama.bmp')),
                (200, 200)),
                (greenfn[1] + 500, 50))

    print(f"{r}, {panorama_x}, {panorama_x_local} -- {panorama_list_extra}")

    pg.display.flip()
    pgp = pg.time.Clock().tick(fps) / 1000
