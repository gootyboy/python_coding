import time
import cv2
import pgzrun
import pygame
from pgzero.clock import clock
from pgzero.actor import Actor
from pgzero.rect import Rect
from pgzero.keyboard import keys
import subprocess
import tempfile

video_path = r"/Users/gootyboy/Desktop/myrepos/python_coding/pygame_game/mini_movie/images/A2.MOV"
TITLE = "Gautam's mini movie"
WIDTH = 800
HEIGHT = 600

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS) if cap.get(cv2.CAP_PROP_FPS) != 0 else 30
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
video_length = total_frames / fps

MOVIE_TIME = int(video_length)
MOUSE_HOVER_TIME = 5  # seconds
THE_END_TIME = 2  # seconds
THANKS_FOR_WATCHING_TIME = 5  # seconds

bg_color = (255, 255, 255)
mouse_hover = False
paused = True
milliseconds_shown = 0
text_y_pos = HEIGHT + 100
credits = ["Directed by Gautam Pulugurta", "Produced by Gautam Pulugurta", "Screenplay by Gautam Pulugurta", "Music Director: Gautam Pulugurta", "Story by Gautam Pulugurta"]
forward_10 = Actor("forward_10", (WIDTH - 120, 280))
backward_10 = Actor("backward_10", (120, 280))
mouse_hover_timer = 0
thanks_for_watching = False
show_credits = False
current_frame = None

pygame.init()
pygame.mixer.init()

# Extract and convert audio from the video using ffmpeg
temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav').name

try:
    subprocess.run([
        'ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', temp_audio_file
    ], check=True)
except subprocess.CalledProcessError as e:
    print("ffmpeg error:", e)

def draw_filled_triangle(color, point_1, point_2, point_3):
    pygame.draw.polygon(screen.surface, color, [point_1, point_2, point_3], 0)

def get_tens_and_ones(number):
    ones_digit = number % 10
    tens_digit = (number // 10) % 10
    return f"{tens_digit}{ones_digit}"

def draw_line(start, end, color, thickness):
    pygame.draw.line(surface=screen.surface, color=color, start_pos=start, end_pos=end, width=thickness)

def draw():
    global bg_color, milliseconds_shown, text_y_pos, show_credits, thanks_for_watching, current_frame
    screen.fill(bg_color)

    if milliseconds_shown <= MOVIE_TIME * 1000:
        if not paused:
            ret, frame = cap.read()
            if ret:
                current_frame = frame
                frame = cv2.resize(current_frame, (WIDTH, HEIGHT))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                screen.blit(frame, (0, 0))
            milliseconds_shown += int(1000 / fps)
        else:
            if current_frame is not None:
                frame = cv2.resize(current_frame, (WIDTH, HEIGHT))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                screen.blit(frame, (0, 0))

        if mouse_hover:
            if paused:
                draw_filled_triangle((200, 200, 200), (400, 250), (400, 325), (475, (250 + 325) / 2))
            else:
                screen.draw.filled_rect(Rect(400, 250, 10, 75), (200, 200, 200))
                screen.draw.filled_rect(Rect(450, 250, 10, 75), (200, 200, 200))

            screen.draw.text(f"{milliseconds_shown // 1000}:{get_tens_and_ones(milliseconds_shown // 10)}", bottomleft=(20, HEIGHT - 20), color=(0, 0, 0))

            remaining_time = (MOVIE_TIME * 1000) - milliseconds_shown
            screen.draw.text(f"{remaining_time // 1000}:{get_tens_and_ones(remaining_time // 10)}", bottomleft=(WIDTH - 50, HEIGHT - 20), color=(0, 0, 0))
            forward_10.draw()
            backward_10.draw()
            draw_line((17, HEIGHT - 10), (WIDTH - 5, HEIGHT - 10), color=(128, 128, 128), thickness=3)
            draw_line((17, HEIGHT - 10), ((((milliseconds_shown / 1000) / MOVIE_TIME) * (WIDTH - 22)) + 17, HEIGHT - 10), color=(255, 0, 0), thickness=3)
    else:
        if not thanks_for_watching:
            screen.fill((0, 0, 0))
            screen.draw.text("THE END!", center=(WIDTH / 2, text_y_pos - 425), color=(255, 255, 255), fontsize=175)
            if show_credits:
                screen.draw.text("Credits", center=(WIDTH / 2, text_y_pos), color=(255, 255, 255), fontsize=100)
                for i in range(len(credits)):
                    screen.draw.text(credits[i], center=(WIDTH / 2, text_y_pos + 100 + 75 * i), color=(255, 255, 255), fontsize=35)
        else:
            screen.fill((0, 0, 0))
            screen.draw.text("Thanks for watching!", center=(WIDTH / 2, HEIGHT / 2), color=(255, 255, 255), fontsize=100)
            screen.draw.text("Part 2 expected to be released in 2027!", center=(WIDTH / 2, HEIGHT / 2 + 100), color=(255, 255, 255), fontsize=50)
            if milliseconds_shown >= (MOVIE_TIME + THE_END_TIME + THANKS_FOR_WATCHING_TIME) * 1000:
                pgzrun.sys.exit()

def update():
    global text_y_pos, milliseconds_shown, credits, thanks_for_watching, show_credits
    if milliseconds_shown >= (MOVIE_TIME + THE_END_TIME) * 1000:
        show_credits = True
    if show_credits:
        if text_y_pos + 100 + 75 * (len(credits) - 1) > 0:
            text_y_pos -= 1
        else:
            thanks_for_watching = True
            cap.release()  # Release video capture once done

def on_mouse_down(pos, button):
    global paused, milliseconds_shown
    if show_credits or milliseconds_shown >= (MOVIE_TIME + THE_END_TIME + THANKS_FOR_WATCHING_TIME) * 1000:
        return  # Disable mouse controls when showing credits or after movie ends
    if button == mouse.LEFT:
        if forward_10.collidepoint(pos):
            if not paused:
                pygame.mixer.music.pause()
            milliseconds_shown += 10000
            cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
            paused = False
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            pygame.mixer.music.set_pos(milliseconds_shown / 1000)
        elif backward_10.collidepoint(pos):
            if not paused:
                pygame.mixer.music.pause()
            milliseconds_shown = max(0, milliseconds_shown - 10000)
            cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
            paused = False
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            pygame.mixer.music.set_pos(milliseconds_shown / 1000)
        elif Rect(380, 225, 100, 125).collidepoint(pos):
            paused = not paused
            if paused:
                cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
                pygame.mixer.music.pause()
            else:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_pos(milliseconds_shown / 1000)

def on_key_down(key):
    global paused, milliseconds_shown, mouse_hover
    if show_credits or milliseconds_shown >= (MOVIE_TIME + THE_END_TIME + THANKS_FOR_WATCHING_TIME) * 1000:
        return  # Disable key controls when showing credits or after movie ends
    if key == keys.SPACE:
        paused = not paused
        if paused:
            cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_pos(milliseconds_shown / 1000)
        mouse_hover = True
    elif key == keys.RIGHT:
        if not paused:
            pygame.mixer.music.pause()
        milliseconds_shown += 10000
        cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
        paused = False
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        pygame.mixer.music.set_pos(milliseconds_shown / 1000)
        mouse_hover = True
    elif key == keys.LEFT:
        if not paused:
            pygame.mixer.music.pause()
        milliseconds_shown = max(0, milliseconds_shown - 10000)
        cap.set(cv2.CAP_PROP_POS_FRAMES, milliseconds_shown * fps / 1000)
        paused = False
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        pygame.mixer.music.set_pos(milliseconds_shown / 1000)
        mouse_hover = True

def on_mouse_move(pos):
    global mouse_hover
    if 0 < pos[0] < WIDTH - 10 and 0 < pos[1] < HEIGHT - 10:
        mouse_hover = True
    else:
        mouse_hover = False

def update_milliseconds_shown():
    global milliseconds_shown
    if not paused:
        milliseconds_shown += 1

def update_mouse_hover():
    global mouse_hover, mouse_hover_timer
    org_mouse_pos = pygame.mouse.get_pos()
    if mouse_hover_timer >= (MOUSE_HOVER_TIME * 100):
        if org_mouse_pos == pygame.mouse.get_pos():
            mouse_hover = False
        else:
            org_mouse_pos = pygame.mouse.get_pos()
        mouse_hover_timer = 0
    else:
        mouse_hover_timer += 1

clock.schedule_interval(update_mouse_hover, 0.01)
clock.schedule_interval(update_milliseconds_shown, 0.01)

pygame.mixer.music.load(temp_audio_file)
# Do not play sound at the start to ensure it starts only when unpaused
pgzrun.go()