from collections import deque

queue = deque(["Simon", "Hagen", "Dorothea"])
print(queue)

print("Jonna und Lotta betreten den Raum.")
queue.append("Lotta")
queue.append("Jonna")
print(queue)

print(queue[0] + " verlässt den Raum.")
queue.popleft()
print(queue)

print(queue[0] + " verlässt den Raum.")
queue.popleft()
print(queue)

print("Jetzt sind " + str(len(queue)) + " Personen im Raum.")
