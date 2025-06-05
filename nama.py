from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)

def draw_cube(x, y, z, sx, sy, sz):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(sx, sy, sz)
    glutSolidCube(1)
    glPopMatrix()

def draw_S():
    draw_cube(0.0, 0.7, 0, 1.0, 0.2, 0.2)
    draw_cube(-0.4, 0.35, 0, 0.2, 0.8, 0.2)
    draw_cube(0.0, 0.0, 0, 1.0, 0.2, 0.2)
    draw_cube(0.4, -0.35, 0, 0.2, 0.8, 0.2)
    draw_cube(0.0, -0.7, 0, 1.0, 0.2, 0.2)

def draw_U():
    draw_cube(-0.4, 0.0, 0, 0.2, 1.4, 0.2)
    draw_cube(0.4, 0.0, 0, 0.2, 1.4, 0.2)
    draw_cube(0.0, -0.7, 0, 0.8, 0.2, 0.2)

def draw_L():
    draw_cube(-0.4, 0.0, 0, 0.2, 1.5, 0.2)
    draw_cube(0.0, -0.7, 0, 1.0, 0.2, 0.2)

def draw_T():
    draw_cube(0.0, 0.7, 0, 1.0, 0.2, 0.2)
    draw_cube(0.0, 0.0, 0, 0.2, 1.5, 0.2)

def draw_A():
    draw_cube(-0.4, 0.0, 0, 0.2, 1.5, 0.2)
    draw_cube(0.4, 0.0, 0, 0.2, 1.5, 0.2)
    draw_cube(0.0, 0.0, 0, 0.8, 0.2, 0.2)
    draw_cube(0.0, 0.6, 0, 0.8, 0.2, 0.2)

def draw_N():
    draw_cube(-0.4, 0.0, 0, 0.2, 1.5, 0.2)  # kiri
    draw_cube(0.4, 0.0, 0, 0.2, 1.5, 0.2)   # kanan
    # diagonal
    for i in range(8):
        x = -0.4 + (i * 0.1)
        y = 0.65 - (i * 0.18)
        draw_cube(x, y, 0, 0.2, 0.2, 0.2)

def draw_word():
    glPushMatrix()
    glTranslatef(-9.0, 0, 0)
    draw_S()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-6.0, 0, 0)
    draw_U()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.0, 0, 0)
    draw_L()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0, 0)
    draw_T()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.0, 0, 0)
    draw_A()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6.0, 0, 0)
    draw_N()
    glPopMatrix()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -25.0)
    glRotatef(angle, 0, 1, 0)

    draw_word()

    glutSwapBuffers()
    angle += 0.5

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h if h != 0 else 1, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

# Main
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"SULTAN in OpenGL")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()
