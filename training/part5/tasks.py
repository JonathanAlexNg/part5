from invoke import task

'''
@task
def name_of_task(c):
    c.run("COMMANDS")
'''


# Call with 'invoke build'
@task
def test(c):
    print("Pyinvoke test message.")


# Main task     # Note that ros_cont is conatiner based on Dockerfile and has been modified
@task
def build(c):
    c.run("sudo docker image rm super-ros-node")
    c.run("sudo docker commit ros_cont super-ros-node:latest")      # Builds image based on ros_cont
    print('\nImage super-ros-node has been created. Any pre-existing has been overwritten.\
        \n\nList of existing images:\n')
    c.run("sudo docker images")

    # If any existing image with that name exist, will overwrite that
    # Maybe task can even get inputs on what to name the image in the future?

# sudo docker run -d --name <container_name> <what image to use>
# sudo docker run -d --name super_cont super-ros-node