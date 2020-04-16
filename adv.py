from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create the traversal graph


def create_graph_from_map():
    # Create graph starting at start room {room_id: exits/neighbors}
    # {
    #     0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    # }
    traversal_map = {}
    num_of_rooms = len(room_graph)

    for room_id in range(0, num_of_rooms):
        exits = {}
        current_room = world.rooms[room_id]

        if current_room.n_to is not None:
            exits["n"] = current_room.n_to.id
        if current_room.s_to is not None:
            exits["s"] = world.rooms[room_id].s_to.id
        if current_room.e_to is not None:
            exits["e"] = world.rooms[room_id].e_to.id
        if current_room.w_to is not None:
            exits["w"] = world.rooms[room_id].w_to.id

        traversal_map[current_room.id] = exits

    print("traversal_map:", traversal_map)


create_graph_from_map()


# def get_neighboring_rooms(room_id):
#     if room_id in world:
#         return self.vertices[vertex_id]
#     else:
#         return None


def get_route():
    # Keep track of explored rooms.
    # Get neighbors of start room, aka, get exits of current room (function)
    # do dft traversal until room has no neighbors, or no exits (function)
    # Then back track (How do we backtrack?) - do a BFS from current room to room with exits == "?"
    # helper function to reverse directions
    pass


# DFT travesal
def dft():
    pass


# Find next node with empty exits
def bfs():
    pass


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
