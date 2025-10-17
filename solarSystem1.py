# =====================================================================
# 🌌 INTERACTIVE SOLAR SYSTEM SIMULATION
# =====================================================================
# Author: [Your Name]
# Created: [Date]
#
# Description:
# This Python program visually simulates our Solar System using the
# Turtle Graphics module combined with a Tkinter-based control panel.
# Each planet orbits the Sun with adjustable speed, and users can:
#   • Zoom in/out to view orbital scales
#   • Pause or resume the animation
#   • Adjust planet sizes
#   • Toggle orbit trails and labels
#   • Click a planet or the Sun to display detailed information
#
# Graphics:
#   • Each celestial body can use a custom GIF (if provided)
#   • If GIFs are missing, color-coded circles are used as fallback
#
# Educational Features:
#   • Clicking an object shows scientific details (mass, type, temperature)
#   • Displays fun facts and planetary descriptions
#
# Dependencies:
#   • turtle — for drawing planets and orbits
#   • tkinter — for control panel UI
#   • math — for trigonometric orbital motion
#   • os/random — for file management and twinkling stars
#
# =====================================================================

# Import required libraries
import turtle              # for graphics and drawing planets
import os                  # for checking image file paths
import random              # for random stars and twinkling
import tkinter as tk       # for GUI buttons (control panel)
from math import *         # for sin, cos, etc. (used in orbit calculations)

# ==== YOUR GIF FILES ====
# Dictionary of all your planet and background images with EXACT paths
gif_files = {
    "sun": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\sun-no-bg.gif",
    "mercury": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\mercury no bg.gif", 
    "venus": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\venus no bg.gif",
    "earth": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\earth-no-bg.gif",
    "mars": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\mars no bg.gif",
    "jupiter": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\jupiter nobg.gif",
    "saturn": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\saturn no bg.gif",
    "uranus": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\uranus no bg.gif",
    "neptune": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\nepton no bg.gif",
    "moon": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\moon no bg.gif",
    "background": r"C:\Users\ASUS TUF\OneDrive\Desktop\solar\background.gif",
}

# ==== Planet Information Database ====
planet_info = {
    "sun": {
        "name": "Sun",
        "type": "Star",
        "diameter": "1,391,000 km",
        "mass": "1.989 × 10³⁰ kg",
        "temperature": "5,500°C (surface)",
        "composition": "71% Hydrogen, 27% Helium, 2% Other",
        "fun_fact": "The Sun contains 99.86% of all mass in our Solar System!",
        "description": "Our Sun is a yellow dwarf star that provides the energy for life on Earth."
    },
    "mercury": {
        "name": "Mercury",
        "type": "Terrestrial Planet",
        "diameter": "4,879 km",
        "mass": "3.301 × 10²³ kg",
        "temperature": "430°C (day), -180°C (night)",
        "orbital_period": "88 Earth days",
        "fun_fact": "A day on Mercury lasts longer than its year!",
        "description": "The smallest and innermost planet, with extreme temperature variations."
    },
    "venus": {
        "name": "Venus",
        "type": "Terrestrial Planet", 
        "diameter": "12,104 km",
        "mass": "4.867 × 10²⁴ kg",
        "temperature": "465°C",
        "orbital_period": "225 Earth days",
        "fun_fact": "Venus rotates backwards compared to other planets!",
        "description": "Often called Earth's sister planet, but with a runaway greenhouse effect."
    },
    "earth": {
        "name": "Earth",
        "type": "Terrestrial Planet",
        "diameter": "12,756 km",
        "mass": "5.972 × 10²⁴ kg",
        "temperature": "15°C (average)",
        "orbital_period": "365.25 days",
        "fun_fact": "Earth is the only known planet with liquid water on its surface!",
        "description": "Our home planet, the only known place in the universe with life."
    },
    "mars": {
        "name": "Mars",
        "type": "Terrestrial Planet",
        "diameter": "6,792 km",
        "mass": "6.417 × 10²³ kg",
        "temperature": "-65°C (average)",
        "orbital_period": "687 Earth days",
        "fun_fact": "Mars has the largest volcano in the Solar System - Olympus Mons!",
        "description": "The Red Planet, with polar ice caps and evidence of past water."
    },
    "jupiter": {
        "name": "Jupiter",
        "type": "Gas Giant",
        "diameter": "142,984 km",
        "mass": "1.898 × 10²⁷ kg",
        "temperature": "-145°C (cloud tops)",
        "orbital_period": "11.86 Earth years",
        "fun_fact": "Jupiter's Great Red Spot is a storm that has raged for over 400 years!",
        "description": "The largest planet, a gas giant with a prominent Great Red Spot."
    },
    "saturn": {
        "name": "Saturn",
        "type": "Gas Giant",
        "diameter": "120,536 km",
        "mass": "5.683 × 10²⁶ kg",
        "temperature": "-178°C (cloud tops)",
        "orbital_period": "29.46 Earth years",
        "fun_fact": "Saturn would float in water if you could find a big enough ocean!",
        "description": "Known for its spectacular ring system made of ice and rock particles."
    },
    "uranus": {
        "name": "Uranus",
        "type": "Ice Giant",
        "diameter": "51,118 km",
        "mass": "8.681 × 10²⁵ kg",
        "temperature": "-224°C",
        "orbital_period": "84 Earth years",
        "fun_fact": "Uranus rotates on its side - practically rolling around the Sun!",
        "description": "An ice giant that rotates on its side with a unique blue-green color."
    },
    "neptune": {
        "name": "Neptune",
        "type": "Ice Giant",
        "diameter": "49,528 km",
        "mass": "1.024 × 10²⁶ kg",
        "temperature": "-218°C",
        "orbital_period": "164.8 Earth years",
        "fun_fact": "Neptune has the strongest winds in the Solar System - over 2,000 km/h!",
        "description": "The windiest planet, a deep blue ice giant with violent storms."
    },
    "moon": {
        "name": "Moon",
        "type": "Natural Satellite",
        "diameter": "3,476 km",
        "mass": "7.342 × 10²² kg",
        "temperature": "127°C (day), -173°C (night)",
        "orbital_period": "27.3 Earth days",
        "fun_fact": "The Moon is slowly moving away from Earth at 3.8 cm per year!",
        "description": "Earth's only natural satellite, responsible for ocean tides."
    }
}

# ==== Verify all files exist ====
print("🖼️ Checking your GIF files...")
available_files = {}
missing_files = []

for key, file_path in gif_files.items():
    if os.path.isfile(file_path):               
        available_files[key] = file_path        
        file_size = os.path.getsize(file_path) / 1024  
        print(f"✅ Found {key}: {os.path.basename(file_path)} ({file_size:.1f}KB)")
    else:
        missing_files.append((key, file_path))  
        print(f"❌ Missing {key}: {file_path}")
        
        directory = os.path.dirname(file_path)
        if os.path.exists(directory):
            files_in_dir = os.listdir(directory)
            similar_files = [f for f in files_in_dir if key in f.lower() and f.endswith('.gif')]
            if similar_files:
                print(f"   🔍 Found similar files: {similar_files}")

if missing_files:
    print(f"\n⚠️ {len(missing_files)} files are missing. Using colored circles as fallback.")
else:
    print(f"\n🎉 All {len(available_files)} GIF files found!")

# ==== Setup Turtle Window ====
win = turtle.Screen()
win.setup(width=1400, height=900)
win.bgcolor("black")
win.title("🌌 Your Personal Solar System - Click Planets for Info!")
win.tracer(0)

if "background" in available_files:
    try:
        win.bgpic(available_files["background"])
        print("🌌 Background loaded successfully!")
    except:
        print("⚠️ Background failed to load, using black background")

# === Draw twinkling stars ===
stars = []
num_stars = 50

print("✨ Creating twinkling stars...")
for _ in range(num_stars):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    star.goto(random.randint(-700, 700), random.randint(-450, 450))
    star.dot(random.randint(1, 3))
    stars.append(star)

def twinkle():
    for star in stars:
        if random.random() < 0.3:
            size = random.uniform(1, 3.5)
            star.clear()
            star.dot(size)
    win.ontimer(twinkle, 300)

twinkle()

# ==== Register all available GIF shapes ====
print("📝 Registering GIF shapes...")
for key, file_path in available_files.items():
    try:
        win.register_shape(file_path)
        print(f"✅ Registered {key}")
    except Exception as e:
        print(f"❌ Failed to register {key}: {e}")

# ==== Information Display System ====
info_display = turtle.Turtle()
info_display.hideturtle()
info_display.penup()
info_display.color("white")
info_display.goto(0, 400)

current_info = None

def show_info(celestial_key):
    """Display information about a celestial body at the TOP"""
    global current_info
    
    if celestial_key not in planet_info:
        return
    
    info = planet_info[celestial_key]
    current_info = celestial_key
    
    info_display.clear()
    info_display.goto(0, 380)
    info_display.color("cyan")
    info_display.write(f"🌌 {info['name']} Information", align="center", font=("Arial", 16, "bold"))
    
    y_position = 350
    info_display.color("white")
    
    facts = [
        f"Type: {info['type']}",
        f"Diameter: {info['diameter']}",
        f"Mass: {info['mass']}",
    ]
    
    if 'temperature' in info:
        facts.append(f"Temperature: {info['temperature']}")
    
    if 'orbital_period' in info and celestial_key != "sun":
        facts.append(f"Orbital Period: {info['orbital_period']}")
    
    if 'composition' in info:
        facts.append(f"Composition: {info['composition']}")
    
    for fact in facts:
        info_display.goto(0, y_position)
        info_display.write(fact, align="center", font=("Arial", 12, "normal"))
        y_position -= 25
    
    info_display.goto(0, y_position - 10)
    info_display.color("lightblue")
    info_display.write(info['description'], align="center", font=("Arial", 11, "italic"))
    
    info_display.goto(0, y_position - 40)
    info_display.color("yellow")
    info_display.write(f"✨ Fun Fact: {info['fun_fact']}", align="center", font=("Arial", 10, "bold"))

def clear_info():
    """Clear the information display"""
    global current_info
    info_display.clear()
    current_info = None

def on_planet_click(x, y):
    """Handle clicks on planets and sun"""
    for planet in planets:
        distance = ((x - planet.xcor()) ** 2 + (y - planet.ycor()) ** 2) ** 0.5
        if distance < 30:
            show_info(planet.info_key)
            return
    
    distance_to_sun = ((x - sun.xcor()) ** 2 + (y - sun.ycor()) ** 2) ** 0.5
    if distance_to_sun < 60:
        show_info("sun")
        return
    
    clear_info()

win.onclick(on_planet_click)

# ==== Sun ====
sun = turtle.Turtle()
if "sun" in available_files:
    sun.shape(available_files["sun"])
    sun.shapesize(stretch_wid=1.2, stretch_len=1.2)
    print("☀️ Sun GIF loaded!")
else:
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(stretch_wid=3, stretch_len=3)
    print("☀️ Using circle sun (no GIF)")

sun.penup()
sun.info_key = "sun"

# ==== Planet class ====
show_labels = True
show_trails = True

class Planet(turtle.Turtle):
    def __init__(self, radius, gif_key, star, offset, size, color, name, size_label, speed, trail=True, info_key=None):
        if gif_key in available_files:
            super().__init__(shape=available_files[gif_key])
            self.using_gif = True
            print(f"🪐 {name}: Using GIF (size: {size})")
        else:
            super().__init__(shape="circle")
            self.color(color)
            self.using_gif = False
            print(f"🪐 {name}: Using colored circle (size: {size})")
        
        self.radius = radius
        self.star = star
        self.offset = offset
        self.angle = 0
        self.name = name
        self.size_label = size_label
        self.base_speed = speed
        self.info_key = info_key or name.lower()
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.penup()

        if trail and show_trails:
            self.trail = turtle.Turtle()
            self.trail.hideturtle()
            self.trail.color(color)
            self.trail.penup()
            self.trail.pensize(1)
            self.trail.goto(self.xcor(), self.ycor())
            self.trail.pendown()
        else:
            self.trail = None

        self.label = turtle.Turtle()
        self.label.hideturtle()
        self.label.penup()
        self.label.color("white")

        self.size_display = turtle.Turtle()
        self.size_display.hideturtle()
        self.size_display.penup()
        self.size_display.color("yellow")

    def move(self):
        x = self.offset + self.radius * cos(self.angle)
        y = self.radius * sin(self.angle) * 0.6
        self.goto(self.star.xcor() + x, self.star.ycor() + y)

        if self.trail and show_trails:
            self.trail.goto(self.xcor(), self.ycor())

        self.label.clear()
        self.size_display.clear()

        if show_labels:
            self.label.goto(self.xcor(), self.ycor() + 25)
            self.label.write(self.name, align="center", font=("Arial", 9, "bold"))

            if self.size_label:
                self.size_display.goto(self.xcor(), self.ycor() - 25)
                self.size_display.write(self.size_label, align="center", font=("Arial", 7, "normal"))

    def reset_position(self):
        self.goto(self.star.xcor() + self.radius + self.offset, self.star.ycor())
        self.angle = 0
        if self.trail:
            self.trail.clear()
            self.trail.penup()
            self.trail.goto(self.xcor(), self.ycor())
            if show_trails:
                self.trail.pendown()

    def toggle_trail(self):
        if self.trail:
            if show_trails:
                self.trail.pendown()
            else:
                self.trail.penup()

# ==== Create planets ====
print("\n🪐 Creating planets with smaller sizes...")
planets = [
    Planet(180, "mercury", sun, 0, 0.15, "gray", "Mercury", "4,879 km", 0.06, info_key="mercury"),
    Planet(220, "venus", sun, 0, 0.18, "orange", "Venus", "12,104 km", 0.045, info_key="venus"),
    Planet(280, "earth", sun, 0, 0.2, "blue", "Earth", "12,756 km", 0.035, info_key="earth"),
    Planet(340, "mars", sun, 0, 0.16, "red", "Mars", "6,792 km", 0.025, info_key="mars"),
    Planet(460, "jupiter", sun, 0, 0.35, "orange", "Jupiter", "142,984 km", 0.015, info_key="jupiter"),
    Planet(560, "saturn", sun, 0, 0.3, "khaki", "Saturn", "120,536 km", 0.012, info_key="saturn"),
    Planet(660, "uranus", sun, 0, 0.22, "cyan", "Uranus", "51,118 km", 0.008, info_key="uranus"),
    Planet(760, "neptune", sun, 0, 0.21, "blue", "Neptune", "49,528 km", 0.006, info_key="neptune"),
]

if len(planets) >= 3:
    moon = Planet(45, "moon", planets[2], 0, 0.08, "lightgray", "Moon", "3,476 km", 0.15, trail=False, info_key="moon")
    planets.append(moon)
    print("🌙 Moon added to Earth (size: 0.08)")

def get_speeds():
    return [p.base_speed for p in planets]

speeds = get_speeds()

print("🎯 Setting initial positions...")
for p in planets:
    p.reset_position()

running = True
speed_multiplier = 1.0

def animate():
    if running:
        win.update()
        for i, p in enumerate(planets):
            p.move()
            p.angle += speeds[i] * speed_multiplier
        win.ontimer(animate, 15)

# ==== Control Functions ====
def toggle_run():
    global running
    running = not running
    run_button.config(text="▶️ Resume" if not running else "⏸️ Pause")
    if running:
        animate()

def increase_speed():
    global speed_multiplier
    speed_multiplier = min(5.0, speed_multiplier * 1.2)
    speed_label.config(text=f"Speed: {speed_multiplier:.1f}x")

def decrease_speed():
    global speed_multiplier
    speed_multiplier = max(0.1, speed_multiplier * 0.8)
    speed_label.config(text=f"Speed: {speed_multiplier:.1f}x")

def reset_simulation():
    global speed_multiplier
    speed_multiplier = 1.0
    speed_label.config(text=f"Speed: {speed_multiplier:.1f}x")
    for p in planets:
        p.reset_position()
    clear_info()

def zoom_in():
    for p in planets:
        if p.name != "Moon":
            p.radius *= 1.15
    for p in planets:
        p.reset_position()

def zoom_out():
    for p in planets:
        if p.name != "Moon":
            p.radius *= 0.85
    for p in planets:
        p.reset_position()

def toggle_labels():
    global show_labels
    show_labels = not show_labels
    labels_button.config(text="🏷️ Show Labels" if not show_labels else "🚫 Hide Labels")
    if not show_labels:
        for p in planets:
            p.label.clear()
            p.size_display.clear()

def toggle_trails():
    global show_trails
    show_trails = not show_trails
    trails_button.config(text="🌀 Show Trails" if not show_trails else "🚫 Hide Trails")
    for p in planets:
        p.toggle_trail()
        if not show_trails and p.trail:
            p.trail.clear()

def make_smaller():
    for p in planets:
        current_size = p.shapesize()[0]
        new_size = max(0.05, current_size * 0.8)
        p.shapesize(stretch_wid=new_size, stretch_len=new_size)
        print(f"📏 Made {p.name} smaller: {current_size:.2f} → {new_size:.2f}")

def make_bigger():
    for p in planets:
        current_size = p.shapesize()[0]
        new_size = min(1.0, current_size * 1.2)
        p.shapesize(stretch_wid=new_size, stretch_len=new_size)
        print(f"📏 Made {p.name} bigger: {current_size:.2f} → {new_size:.2f}")

def clear_info_display():
    clear_info()

# ==== Tkinter GUI (Control Panel) ====
print("🎮 Creating control panel...")
root = tk.Tk()
root.title("🌌 Solar System Control Panel")
root.geometry("300x650")
root.configure(bg='black')

title_label = tk.Label(root, text="🌌 Solar System Controls", fg="white", bg="black", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

run_button = tk.Button(root, text="⏸️ Pause", command=toggle_run, width=20, bg="darkgreen", fg="white", font=("Arial", 10, "bold"))
run_button.pack(pady=5)

speed_frame = tk.Frame(root, bg="black")
speed_frame.pack(pady=10)

tk.Button(speed_frame, text="🚀 Speed Up", command=increase_speed, bg="blue", fg="white", width=10).pack(side=tk.LEFT, padx=2)
tk.Button(speed_frame, text="🐌 Slow Down", command=decrease_speed, bg="purple", fg="white", width=10).pack(side=tk.RIGHT, padx=2)

speed_label = tk.Label(root, text=f"Speed: {speed_multiplier:.1f}x", fg="yellow", bg="black", font=("Arial", 10))
speed_label.pack()

zoom_frame = tk.Frame(root, bg="black")
zoom_frame.pack(pady=10)

tk.Button(zoom_frame, text="🔍 Zoom In", command=zoom_in, bg="darkblue", fg="white", width=10).pack(side=tk.LEFT, padx=2)
tk.Button(zoom_frame, text="🔍 Zoom Out", command=zoom_out, bg="darkred", fg="white", width=10).pack(side=tk.RIGHT, padx=2)

size_frame = tk.Frame(root, bg="black")
size_frame.pack(pady=10)

tk.Button(size_frame, text="📏 Smaller", command=make_smaller, bg="brown", fg="white", width=10).pack(side=tk.LEFT, padx=2)
tk.Button(size_frame, text="📏 Bigger", command=make_bigger, bg="darkorange", fg="white", width=10).pack(side=tk.RIGHT, padx=2)

labels_button = tk.Button(root, text="🚫 Hide Labels", command=toggle_labels, width=20, bg="darkgray", fg="white")
labels_button.pack(pady=5)

trails_button = tk.Button(root, text="🚫 Hide Trails", command=toggle_trails, width=20, bg="darkgray", fg="white")
trails_button.pack(pady=5)

info_button = tk.Button(root, text="🗑️ Clear Info", command=clear_info_display, width=20, bg="darkblue", fg="white")
info_button.pack(pady=5)

reset_button = tk.Button(root, text="🔄 Reset Everything", command=reset_simulation, width=20, bg="darkred", fg="white", font=("Arial", 10, "bold"))
reset_button.pack(pady=15)

status_frame = tk.Frame(root, bg="black")
status_frame.pack(pady=10)

tk.Label(status_frame, text="📊 Status:", fg="white", bg="black", font=("Arial", 10, "bold")).pack()
tk.Label(status_frame, text=f"GIFs Found: {len(available_files)}/{len(gif_files)}", fg="lime", bg="black").pack()
tk.Label(status_frame, text=f"Planets: {len(planets)}", fg="cyan", bg="black").pack()
tk.Label(status_frame, text="☀️ Sun size: 1.2", fg="yellow", bg="black").pack()
tk.Label(status_frame, text="💡 Click planets for info!", fg="yellow", bg="black", font=("Arial", 9, "bold")).pack()

if missing_files:
    tk.Label(status_frame, text=f"Missing: {len(missing_files)} files", fg="red", bg="black").pack()

instructions = tk.Text(root, height=8, width=35, bg="black", fg="white", font=("Arial", 8))
instructions.pack(pady=10)
instructions.insert(tk.END, "🎮 INSTRUCTIONS:\n\n")
instructions.insert(tk.END, "• CLICK any planet for info!\n")
instructions.insert(tk.END, "• Info appears at TOP\n")
instructions.insert(tk.END, "• Pause/Resume animation\n") 
instructions.insert(tk.END, "• Zoom in/out for better view\n")
instructions.insert(tk.END, "• Adjust planet sizes\n")
instructions.insert(tk.END, "• Toggle labels and trails\n")
instructions.insert(tk.END, "• Clear info with button\n")
instructions.insert(tk.END, "• Reset to start over\n\n")
instructions.insert(tk.END, "Click the Sun or planets to learn! 🌌")
instructions.config(state=tk.DISABLED)

# ==== Start everything ====
print("\n🚀 Starting solar system simulation...")
print("🎮 Control panel is ready!")
print("💡 Click on any planet or the sun to see information!")
print("📄 Information now displays at the TOP of the screen!")
print("✨ All planets are smaller for better viewing!")

animate()
root.mainloop()