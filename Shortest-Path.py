import heapq
import tkinter as tk
from tkinter import ttk

# Define your places and their coordinates
places = {
    "School Entrance": (400, 20),
    "b1":(460,50),
          "b8":(480,50),
          "b9":(440,50),
          "b10":(420,50),
          "b11":(500,50),
          "b12":(380,50),
          "b13":(360,50),
          "b14":(340,50),
          "b15":(320,50),
          "b16":(300,50),
          "b17":(280,50),

    "b2":(550,180),
        "b3":(570,180),
            "b4":(550,200),
              "b5":(550,220),
               "b6":(570,220),
                "b7":(570,200),
    "PL1":(430,200),
      "PL2":(450,200),
        "PL3":(430,220),
          "PL4":(450,220),
            "PL5":(450,240),
              "PL6":(430,240),
                "PL7":(450,180),
                  "PL8":(430,180),
                    "PL9":(470,220),
                      "PL10":(470,240),
                        "PL11":(470,200),
                          "PL12":(470,180),
                            "PL13":(410,180),
                              "PL14":(410,200),
                                "PL15":(410,220),
                                  "PL16":(410,240),
                                    "PL17":(390,200),
                                      "PL18":(390,220),
                                        "PL19":(370,240),
                                          "PL20":(370,220),
                                            "PL21":(390,240),
                                            "PL22":(350,240),
                                            "PL23":(330,240),
                                            "PL24":(350,220),
                                            "PL25":(330,220),

    "Stair case": (400, 80),
    "East wing": (520, 80),
    "West wing":(280,80),
    "Planning":(260,150),
    "Building Estates":(260,180),
    "Exit":(260,280),
    "ROTC Office":(260,360),
    "Dance Studio":(350,360),
        "PL26":(250,400),
        "PL27":(270,400),
        "PL28":(290,400),
        "PL29":(310,400),
        "PL30":(330,400),   

    "UPO": (520, 150),
    "VP-Admin":(470,150),
    "VP-ACAD":(430,150),
    "HRMO":(380,150),
    "Registrar":(350,180),
    "Administration": (600, 150),
    "Records": (600, 200),
    "Accounting": (600, 240),

    "Supply":(520,240),
    "COA":(520,280,),
    "HM":(480,280),
    "NSTP":(430,280),

    "Cashier": (600, 280),
    "Budget": (600, 320),
                "WL47":(560,300),   
                 "WL37":(550,260),   
                "WL38":(550,280),   
                "WL39":(540,310),   
                 "WL40":(520,310),   
                 "WL41":(500,310),   
                 "WL42":(480,310),   
                 "WL43":(460,310),   
                 "WL44":(440,310),  
                 "WL45":(420,310),   
                 "WL46":(400,310),    

    "Building": (600, 360),
    "Canteen": (600, 440),
    "Bakery":(530,440),
    "Stair case three":(480, 440),
    "SSG": (480,470),
    "Library": (380,440),
         "PL31":(400,400),   
          "PL32":(420,400),   
           "PL33":(440,400),   
            "PL34":(460,400),  
             "PL35":(480,400),   
              "PL36":(500,400),   
               "PL37":(520,400),   
                "PL38":(540,400), 
                 "PL39":(560,400),      
    "Clinic":(330,440),
    "SA":(280,440),
}

# Define paths between locations with weights
paths = {
    ("School Entrance", "Stair case"): 1,
    ("Stair case", "East wing"): 2,
    ("Stair case","VP-ACAD"):4,
    

    ("Stair case","West wing"):3,
    ("West wing","Planning"):4,
    ("Planning","Building Estates"):5,
    ("Building Estates","Registrar"):6,
    ("Building Estates","Exit"):6,
    ("Exit","ROTC Office"):7,
    ("ROTC Office","Dance Studio"):8,
    ("Dance Studio","Library"):9,

    ("East wing", "Administration"): 3,
    ("East wing", "UPO"): 1,
    ("Administration", "Records"): 4,
    ("UPO", "Administration"): 2,
    ("UPO","Supply"):2,

    ("UPO","VP-Admin"):2,
    ("VP-Admin","VP-ACAD"):3,
    ("VP-ACAD","HRMO"):4,
    ("HRMO","Registrar"):5,
    ("Records", "Accounting"): 5,
    ("Accounting","Supply"):6,
    ("Supply","COA"):7,
    ("COA","HM"):8,
    ("HM","NSTP"):9,

    ("Accounting", "Cashier"): 6,
    ("Cashier", "Budget"): 7,
    ("Budget", "Building"): 8,
    ("Building","Canteen"):9,
    ("Canteen","Bakery"):10,
    ("Bakery","Stair case three"):12,
    ("Stair case three","SSG"):13,
    ("Stair case three","Library"):14,
    ("Library","Clinic"):15,
    ("Clinic","SA"):16,
}

# Convert paths to an adjacency list
adjacency_list = {}
for (start, end), cost in paths.items():
    if start not in adjacency_list:
        adjacency_list[start] = {}
    if end not in adjacency_list:
        adjacency_list[end] = {}
    adjacency_list[start][end] = cost
    adjacency_list[end][start] = cost

# Create a grid to represent the map
grid = [[0] * 800 for _ in range(800)]  # Initialize grid with zeros


# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, goal):
    # Initialize the priority queue and visited set
    queue = [(0, start, [])]  # Include a list to store the path
    visited = set()

    # While the priority queue is not empty
    while queue:
        # Dequeue the current node, cost, and path
        cost, current, path = heapq.heappop(queue)

        # If this node has not been visited yet
        if current not in visited:
            # Mark this node as visited
            visited.add(current)

            # If this is the goal node, we are done
            if current == goal:
                return cost, path + [current]  # Return the path as well

            # Otherwise, enqueue all neighbors with updated costs
            for neighbor, edge_cost in graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [current]))

    # If we get here, there is no path between the start and goal
    return None

# Define the main GUI window
root = tk.Tk()
root.title("Surigao Del Norte State University Ground Floor Map")

# Create a canvas to draw the map
canvas = tk.Canvas(root, width=900, height=650)
canvas.pack()

# Draw paths
for (start, end), cost in paths.items():
    (x1, y1), (x2, y2) = places[start], places[end]
    canvas.create_line(x1, y1, x2, y2, fill="black", tags="path", width=2)
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(cost), fill="black", tags="path_cost")

# Draw places
for place, (x, y) in places.items():
    canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="green")
    canvas.create_text(x + 20, y, text=place, anchor="w")

# Create a frame to hold the start and goal labels and entry fields
frame = ttk.Frame(root, padding="10")
frame.pack()

# Create labels for start and goal
start_label = ttk.Label(frame, text="Starting point:")
start_label.grid(row=0, column=0)

goal_label = ttk.Label(frame, text="Goal:")
goal_label.grid(row=1, column=0)

# Create drop-down menus for selecting start and goal locations
start_var = tk.StringVar()
start_dropdown = ttk.Combobox(frame, textvariable=start_var, values=list(places.keys()))
start_dropdown.grid(row=0, column=1)

goal_var = tk.StringVar()
goal_dropdown = ttk.Combobox(frame, textvariable=goal_var, values=list(places.keys()))
goal_dropdown.grid(row=1, column=1)

# Create a label to display the shortest path
shortest_path_label = ttk.Label(root, text="Shortest Path:")
shortest_path_label.pack()

# Create a label to display the places of the shortest path
shortest_path_places = tk.StringVar()
shortest_path_places_label = ttk.Label(root, textvariable=shortest_path_places)
shortest_path_places_label.pack()

# Create a button to find the shortest path
def animate_path():
    start = start_var.get()
    goal = goal_var.get()

    shortest_path_label.config(text="Searching...")
    root.update()

    result = dijkstra_shortest_path(adjacency_list, start, goal)

    if result is not None:
        path_length, path = result
        shortest_path_label.config(text=f"Shortest Path Found: {path_length}")
        shortest_path_places.set(" -> ".join(path))  # Set the places of the shortest path


        # Draw the shortest path in red
        for i in range(len(path) - 1):
            (x1, y1), (x2, y2) = places[path[i]], places[path[i + 1]]
            canvas.create_line(x1, y1, x2, y2, fill="red", tags="shortest_path", width=2)

    else:
        shortest_path_label.config(text="No path found")

# Create a button to find the shortest path
find_button = ttk.Button(frame, text="Find Shortest Path", command=animate_path)
find_button.grid(row=2, columnspan=2)

# Start the GUI main loop
root.mainloop()