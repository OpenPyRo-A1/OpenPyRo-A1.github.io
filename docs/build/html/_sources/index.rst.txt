.. OpenPyRo-A1 Docs documentation master file, created by
   sphinx-quickstart on Mon Mar 17 20:33:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. title:: OpenPyRo-A1 Docs


Introduction
============
Welcome to the `OpenPyRo-A1 <https://openpyro-a1.github.io/>`_ documentation! This website hosts the hardware assembly guide and usage instructions for our open-source robot.

.. image:: ./_static/images/paper/openpyroa1.png
   :alt: OpenPyRo-A1
   :align: center
   :width: 600

.. Key Features of OpenPyRo-A1
.. ---------------------------

.. - **Affordability:** Priced at approximately $14,000, the OpenPyRo-A1 offers a cost-effective solution for researchers and developers seeking a dual-arm robotic platform.

.. - **Modular Hardware Design:** Constructed using 3D-printed components and CNC-machined aluminum alloy parts, the robot's modular design facilitates easy assembly, maintenance, and customization.

.. - **Advanced Software Integration:** The Python-based software framework supports VR-based data collection, imitation learning from visual and positional data, and seamless integration with LLMs and VLMs for high-level task planning.

.. - **Bimanual Manipulation:** Equipped with two 7-degree-of-freedom (7-DoF) arms, the OpenPyRo-A1 is capable of performing complex bimanual tasks, including object manipulation, cooking, and collaborative operations.

This assembly guide will provide step-by-step instructions to help you build your OpenPyRo-A1 robot, ensuring a smooth and efficient assembly process.

Hardware Design
---------------

We consider the following three key principles when designing OpenPyRo-A1:

**Low-cost:**
The robotic system is designed to be cost-effective while maintaining high performance. To minimize manufacturing expenses, the structure integrates 3D-printed components for non-load-bearing parts and CNC-machined aluminum alloy for critical structural elements.

**Ease of repair:**
Features a modular design with accessible panels, standardized fasteners, color-coded wiring, and quick-release connections, facilitating straightforward maintenance.

**Scalability:**
Supports modular firmware updates and includes pre-drilled expansion points, allowing seamless integration of new technologies.


.. Control System
.. --------------
.. We developed the distributed teleoperation system based on LCM to control the robot, the whole system design as follows:

.. (Pd Control and Gripper) we run this node to do the pd control, the main work for this node including publish robot state such as joint state, gripper state and calculate the control target and set the motor to the target with a stable frequency.

.. (Meta quest3 node) we run this node to publish the original data comes from VR device, such as head and hand pose with a high frquency.

.. (End effetor node) we run this node to calculate forward kinematic result.

.. (Gripper mapper) we run this code to do the data transformer comes from VR device, with this can be very easy to used in different type gripper

.. (calibration node) we run this node to do the calibration from VR to robot frame, to do the smooth control

.. (IK node) we run this to do the innverse kinematic calculation and set the ik solution to the pd control node to control the motor













Bill of materials (BOM)
============================================

Motors
------

.. raw:: html

   Joint motors procurement website: <a href="http://www.eyoubot.com/" target="_blank" rel="noopener noreferrer">link</a><br>
   Gripper motors procurement website: <a href="https://www.mdmbot.com/" target="_blank" rel="noopener noreferrer">link</a>

.. |ph25b_motor| image:: ./_static/images/motors/ph25b.png
   :align: middle
   :width: 100px
   :alt: motor used for waist and chest

.. |ph20b_motor| image:: ./_static/images/motors/ph20b.png
   :align: middle
   :width: 100px
   :alt: motor used for arm

.. |ph17b_motor| image:: ./_static/images/motors/ph17b.png
   :align: middle
   :width: 100px
   :alt: motor used for arm

.. |ph14b_motor| image:: ./_static/images/motors/ph14b.png
   :align: middle
   :width: 100px
   :alt: motor used for arm

.. |ph11b_motor| image:: ./_static/images/motors/ph11b.png
   :align: middle
   :width: 100px
   :alt: motor used for arm

.. |damiao_motor| image:: ./_static/images/motors/damiao.png
   :align: middle
   :width: 100px
   :alt: motor used for grippers


.. csv-table:: material statement for motors
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "waist and chest", "|ph25b_motor|", "2", "motor model: ph25b"
   "arm motor 1", "|ph20b_motor|", "2", "motor model: ph20b"
   "arm motor 2,3", "|ph17b_motor|", "4", "motor model: ph17b"
   "arm motor 4,5", "|ph14b_motor|", "4", "motor model: ph17b"
   "arm motor 6,7", "|ph11b_motor|", "4", "motor model: ph14b"
   "gripper motor", "|damiao_motor|", "2", "motor model: DM-J4310-2EC"




Body structure components
-------------------------
.. Please download the raw step files here: `sample_project.zip <_static/sample_project.zip>`_

.. |base_plate| image:: ./_static/images/structure_components/base_plate.png
   :align: middle
   :width: 100px
   :alt: base plate that supports the upper body of the robot

.. |waist_rotation| image:: ./_static/images/structure_components/waist_rotation.png
   :align: middle
   :width: 100px
   :alt: support the rotation of the waist

.. |waist_motor_left_fixing_part| image:: ./_static/images/structure_components/waist_motor_left_fixing_part.png
   :align: middle
   :width: 100px
   :alt: used to fix the waist motor

.. |waist_motor_right_fixing_part| image:: ./_static/images/structure_components/waist_motor_right_fixing_part.png
   :align: middle
   :width: 100px
   :alt: used with waist motor fixing plate for waist movement

.. |waist_motor_upper_plate| image:: ./_static/images/structure_components/waist_motor_upper_plate.png
   :align: middle
   :width: 100px
   :alt: matched with the left and right fixing plates of the waist motor

.. |chest_plate| image:: ./_static/images/structure_components/chest_plate.png
   :align: middle
   :width: 100px
   :alt: front and rear panels of the torso

.. |scapular_left| image:: ./_static/images/structure_components/scapular_left.png
   :align: middle
   :width: 100px
   :alt: the shoulder part is used to fix the front and rear chest plates

.. |scapular_right| image:: ./_static/images/structure_components/scapular_right.png
   :align: middle
   :width: 100px
   :alt: the shoulder part is used to fix the front and rear chest plates

.. |head_plate| image:: ./_static/images/structure_components/head_plate.png
   :align: middle
   :width: 100px
   :alt: used to supporte head

.. |shoulder_plate_a| image:: ./_static/images/structure_components/shoulder_plate_a.png
   :align: middle
   :width: 100px
   :alt: shoulder motor connection plate

.. |shoulder_plate_b| image:: ./_static/images/structure_components/shoulder_plate_b.png
   :align: middle
   :width: 100px
   :alt: shoulder motor connection plate

.. |upper_arm| image:: ./_static/images/structure_components/upper_arm.png
   :align: middle
   :width: 100px
   :alt: arm motor 2 and 3 connection component

.. |forearm_left| image:: ./_static/images/structure_components/forearm_left.png
   :align: middle
   :width: 100px
   :alt: arm motor 4 and 5 connection component

.. |forearm_right| image:: ./_static/images/structure_components/forearm_right.png
   :align: middle
   :width: 100px
   :alt: arm motor 4 and 5 connection component

.. |elbow_left| image:: ./_static/images/structure_components/elbow_left.png
   :align: middle
   :width: 100px
   :alt: arm motor 3 and 4 connection component

.. |elbow_right| image:: ./_static/images/structure_components/elbow_right.png
   :align: middle
   :width: 100px
   :alt: arm motor 3 and 4 connection component

.. |upper_wrist| image:: ./_static/images/structure_components/upper_wrist.png
   :align: middle
   :width: 100px
   :alt: suite for arm motor 5

.. |wrist_flange| image:: ./_static/images/structure_components/wrist_flange.png
   :align: middle
   :width: 100px
   :alt: suite for arm motor 5

.. csv-table:: material statement for structure components
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "base plate", "|base_plate|", "1", "which supports the upper body of the robot"
   "waist rotation", "|waist_rotation|", "1", "support the rotation of the waist"
   "waist left fixing", "|waist_motor_left_fixing_part|", "1", "used to fix the waist motor"
   "waist right fixing", "|waist_motor_right_fixing_part|", "1", "used with waist motor fixing plate"
   "waist upper plate", "|waist_motor_upper_plate|", "1", "matched with the left and right fixing plates"
   "chest plate", "|chest_plate|", "2", "front and rear panels of the torso"
   "scapular left", "|scapular_left|", "1", "used to fix the front and rear chest plates"
   "scapular right", "|scapular_right|", "1", "used to fix the front and rear chest plates"
   "head plate", "|head_plate|", "1", "used for supporting head"
   "shoulder plate a", "|shoulder_plate_a|", "2", "shoulder motor connection plate a"
   "shoulder plate b", "|shoulder_plate_b|", "2", "shoulder motor connection plate b"
   "upper arm", "|upper_arm|", "2", "arm motor 2 and 3 connection component"
   "elbow left", "|elbow_left|", "2", "arm motor 3 and 4 connection component"
   "elbow right", "|elbow_right|", "2", "arm motor 3 and 4 connection component"
   "forearm left", "|forearm_left|", "2", "arm motor 4 and 5 connection component"
   "forearm right", "|forearm_right|", "2", "arm motor 4 and 5 connection component"
   "upper wrist", "|upper_wrist|", "2", "suite for arm motor 5"
   "wrist flange", "|wrist_flange|", "2", "flange for arm motor 5 and 6 connection"




Screws
------

.. |M3X30| image:: ./_static/images/screw/M3X30.png
   :align: middle
   :width: 100px
   :alt: M3X30

.. |M3X45| image:: ./_static/images/screw/M3X45.png
   :align: middle
   :width: 100px
   :alt: M3X45

.. |M4X16| image:: ./_static/images/screw/M4X16.png
   :align: middle
   :width: 100px
   :alt: M4X16

.. |M4X30| image:: ./_static/images/screw/M4X30.png
   :align: middle
   :width: 100px
   :alt: M4X30

.. |M4X45| image:: ./_static/images/screw/M4X45.png
   :align: middle
   :width: 100px
   :alt: M4X45

.. |M6X12| image:: ./_static/images/screw/M6X12.png
   :align: middle
   :width: 100px
   :alt: M6X12

.. |M6X22| image:: ./_static/images/screw/M6X22.png
   :align: middle
   :width: 100px
   :alt: M6X22

.. |M8X20| image:: ./_static/images/screw/M8X20.png
   :align: middle
   :width: 100px
   :alt: M8X20


.. csv-table:: material statement for screws
   :header: "Name", "Image"
   :widths: 50, 50
   :class: white-background

   "M3X30", "|M3X30|"
   "M3X45", "|M3X45|"
   "M4X16", "|M4X16|"
   "M4X30", "|M4X30|"
   "M4X45", "|M4X45|"
   "M6X12", "|M6X12|"
   "M6X22", "|M6X22|"
   "M8X20", "|M8X20|"

Mechanical components
---------------------

.. |RU66_bearing| image:: ./_static/images/mechanical_components/RU66_bearing.png
   :align: middle
   :width: 100px
   :alt: RU66_bearing


.. csv-table:: material statement for mechanical components
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "bearing", "|RU66_bearing|", "1", "used for connecting chest motor and structural parts"



Tools
-----

.. |screw_glue| image:: ./_static/images/tools/screw_glue.png
   :align: middle
   :width: 100px
   :alt: used to prevent the screws from loosening

.. |hexagon_wrench| image:: ./_static/images/tools/hexagon_wrench.png
   :align: middle
   :width: 100px
   :alt: used to tighten the screws

.. |torque_wrench| image:: ./_static/images/tools/torque_wrench.png
   :align: middle
   :width: 100px
   :alt: set torque to avoid screw stripping

.. |vise| image:: ./_static/images/tools/vise.png
   :align: middle
   :width: 100px
   :alt: securely hold an object in place

.. |wire_strippers| image:: ./_static/images/tools/wire_strippers.png
   :align: middle
   :width: 100px
   :alt: stripping wires

.. |multifunctional_wire_stripper| image:: ./_static/images/tools/multifunctional_wire_stripper.png
   :align: middle
   :width: 100px
   :alt: multifunctional wire stripper

.. |locking_pilers| image:: ./_static/images/tools/locking_pliers.png
   :align: middle
   :width: 100px
   :alt: pulling out pins

.. |diagonal_cutting_pliers| image:: ./_static/images/tools/diagonal_cutting_pliers.png
   :align: middle
   :width: 100px
   :alt: cutting wires

.. |soldering_station_fixture| image:: ./_static/images/tools/soldering_station_fixture.png
   :align: middle
   :width: 100px
   :alt: fix components and facilitate welding

.. |torque_screwdriver| image:: ./_static/images/tools/torque_screwdriver.png
   :align: middle
   :width: 100px
   :alt: fix components and facilitate welding

.. |usb_red_can| image:: ./_static/images/tools/usb_red_can.png
   :align: middle
   :width: 100px
   :alt: connect to motor for testing

.. |power| image:: ./_static/images/tools/power.png
   :align: middle
   :width: 100px
   :alt: provide 48V voltage



.. csv-table:: material statement for tools
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "screw glue", "|screw_glue|", "1", "used to prevent the screws from loosening"
   "hexagon wrench", "|hexagon_wrench|", "1", "used to tighten the screws"
   "torque wrench", "|torque_wrench|", "1", "set torque to avoid screw stripping"
   "vise", "|vise|", "1", "securely hold an object in place"
   "wire stripper", "|wire_strippers|", "1", "stripping wires"
   "wire stripper", "|multifunctional_wire_stripper|", "1", "stripping wires"
   "locking pilers", "|locking_pilers|", "1", "pulling out pins"
   "diagonal pliers", "|diagonal_cutting_pliers|", "1", "cutting wires"
   "soldering fixture", "|soldering_station_fixture|", "1", "fix components and facilitate welding"
   "torque screwdriver", "|torque_screwdriver|", "1", "set torque to avoid screw stripping"
   "usb red can", "|usb_red_can|", "1", "connect to motor for testing"
   "power", "|power|", "1", "provide 48V voltage"


Accessories
-----------

.. |XT30U_m_connector| image:: ./_static/images/accessories/XT30U_m_connector.png
   :align: middle
   :width: 100px
   :alt: used for lithium battery plug

.. |cold_pressed_round_terminal| image:: ./_static/images/accessories/cold_pressed_round_terminal.png
   :align: middle
   :width: 100px
   :alt: used for electrical connection

.. |plastic_shell| image:: ./_static/images/accessories/plastic_shell.png
   :align: middle
   :width: 100px
   :alt: 

.. |lead_free_solder_wire| image:: ./_static/images/accessories/lead_free_solder_wire.png
   :align: middle
   :width: 100px
   :alt: 

.. |reed| image:: ./_static/images/accessories/reed.png
   :align: middle
   :width: 100px
   :alt: 

.. |silicone_wire| image:: ./_static/images/accessories/silicone_wire.png
   :align: middle
   :width: 100px
   :alt: 

.. |power_wire_13AWG| image:: ./_static/images/accessories/power_wire_13AWG.png
   :align: middle
   :width: 100px
   :alt: 

   


.. csv-table:: material statement for accessories
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "XT30U m connector", "|XT30U_m_connector|", "1", "used for lithium battery plug"
   "cold pressed round terminal", "|cold_pressed_round_terminal|", "1", "used for electrical connection"
   "plastic shell", "|plastic_shell|", "1", ""
   "lead free solder wire", "|lead_free_solder_wire|", "1", ""
   "reed", "|reed|", "1", ""
   "silicone_wire", "|silicone_wire|", "1", ""
   "power_wire_13AWG", "|power_wire_13AWG|", "1", "power wire material"







Power system
============

Power wire
-----------
The power module provides 48V voltage, making power wire for power.



Material statement
++++++++++++++++++

.. csv-table:: material statement for power system
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "power", "|power|", "1", "provide 48V voltage"
   "XT30U m connector", "|XT30U_m_connector|", "1", "used for lithium battery plug"
   "cold pressed round terminal", "|cold_pressed_round_terminal|", "1", "used for electrical connection"
   "wire strippers", "|wire_strippers|", "1", "stripping wires"
   "diagonal pliers", "|diagonal_cutting_pliers|", "1", "cutting wires"
   "power_wire_13AWG", "|power_wire_13AWG|", "1", "power wire material"



Assemble video(4X speed)
++++++++++++++++++++++++

.. video:: ./_static/videos/power_wire.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:







CAN system
============================================


CAN wire
-----------
Produce CAN signal wire for communication between CAN device and motors.

Material statement
++++++++++++++++++

.. csv-table:: material statement for can wire
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "reed", "|reed|", "1", ""
   "silicone_wire", "|silicone_wire|", "1", ""
   "wire strippers", "|wire_strippers|", "1", "stripping wires"
   "wire stripper", "|multifunctional_wire_stripper|", "1", "stripping wires"
   "diagonal pliers", "|diagonal_cutting_pliers|", "1", "cutting wires"



Assemble video(4X speed)
++++++++++++++++++++++++

.. video:: ./_static/videos/signal_wire.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:






Integration
============================================

This page will guide you through the process of assembling all components into the robot.



Waist motor
-----------
The waist motor provides the robot with the ability to rotate left and right. Please follow the instructions to assemble.



Material statement
++++++++++++++++++

.. csv-table:: material statement for waist
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "waist motor", "|ph25b_motor|", "2", "motor model: ph25b, please `see <#>`_"
   "base plate", "|base_plate|", "1", "support the upper body of the robot"
   "hexagon wrench", "|hexagon_wrench|", "1", "used to tighten the screws"
   "torque wrench", "|torque_wrench|", "1", "set torque to avoid screw stripping"
   "M8X20", "|M8X20|", "6", "fix plate and table"
   "M4X45", "|M4X45|", "13", "fix waist motor and plate"


Assemble video(4X speed)
++++++++++++++++++++++++

.. video:: ./_static/videos/waist.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:


Chest motor
-----------
The chest provide with one freedom to turn up and down, what we need as follows. Please follow the instructions to assemble.


Material statement
++++++++++++++++++

.. csv-table:: material statement for chest
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "chest motor", "|ph25b_motor|", "2", "motor model: ph25b, please `see <#>`_"
   "waist left fixing", "|waist_motor_left_fixing_part|", "1", "used to fix the waist motor"
   "waist right fixing", "|waist_motor_right_fixing_part|", "1", "used with waist motor fixing plate"
   "waist upper plate", "|waist_motor_upper_plate|", "1", "matched with the left and right fixing plates"
   "waist rotation", "|waist_rotation|", "1", "support the rotation of the waist"
   "hexagon wrench", "|hexagon_wrench|", "1", "used to tighten the screws"
   "bearing", "|RU66_bearing|", "1", "used for connecting chest motor and structural parts"
   "M4X30", "|M4X30|", "32", "fix components"
   "M4X45", "|M4X45|", "12", "fix components"
   "M4X16", "|M4X16|", "16", "fix components"
   "M6X12", "|M6X12|", "6", "fix components"



Assemble video(4X speed)
++++++++++++++++++++++++

Firstly, assemble the chest motor and its components.

.. video:: ./_static/videos/chest.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:


Secondly, assemble chest motor turntable components.

.. video:: ./_static/videos/chest_turnable.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:



Right shoulder motor
--------------------
From the perspective of the robot, the first motor of the right arm, what we need as follows. Please follow the instructions to assemble.

Material statement
++++++++++++++++++

.. csv-table:: material statement for right shoulder
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "scapular_right", "|scapular_right|", "1", "used to fix the front and rear chest plates"
   "arm motor 1", "|ph20b_motor|", "1", "motor model: ph20b"
   "shoulder plate a", "|shoulder_plate_a|", "1", "shoulder motor connection plate a"
   "M6X22", "|M6X22|", "8", "fix scapular right and chest plates"
   "M3X45", "|M3X45|", "8", "fix right shoulder motor and right scapular"
   "M3X30", "|M3X30|", "14", "fix shoulder plate a and right motor"
   "torque wrench", "|torque_wrench|", "1", "set torque to avoid screw stripping"
   "hexagon wrench", "|hexagon_wrench|", "1", "used to tighten the screws"


Assemble video(4X speed)
++++++++++++++++++++++++


.. video:: ./_static/videos/right_motor_1.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:






Waist motor zero adjustment
---------------------------
The waist motor is adjusted to its zero position through software.

Material Statement
++++++++++++++++++

.. csv-table:: material statement for waist motor zero position adjustment
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "usb red can", "|usb_red_can|", "1", "connect to motor for testing"
   "M3X30", "|M3X30|", "1", "fix support plate and waist motor"
   "locking pilers", "|locking_pilers|", "1", "pulling out pins"
   "power", "|power|", "1", "provide 48V voltage"







Assemble video(4X speed)
++++++++++++++++++++++++

.. video:: ./_static/videos/waist_motor_zero_adjustment.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:



