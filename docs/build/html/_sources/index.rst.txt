.. OpenPyRo-A1 Docs documentation master file, created by
   sphinx-quickstart on Mon Mar 17 20:33:45 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============
Welcome to the `OpenPyRo-A1 <https://openpyro-a1.github.io/>`_ documentation! This website hosts the hardware assembly guide and usage instructions for our open-source robot.

.. image:: ./_static/images/paper/OpenPyRo-A1.png
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

   "waist and chest", "|ph25b_motor|", "2", "motor model: ph25b, please `see <#>`_"
   "arm motor 1", "|ph20b_motor|", "2", "motor model: ph20b, please `see <#>`_"
   "arm motor 2,3", "|ph17b_motor|", "4", "motor model: ph17b, please `see <#>`_"
   "arm motor 4,5", "|ph14b_motor|", "4", "motor model: ph17b, please `see <#>`_"
   "arm motor 6,7", "|ph11b_motor|", "4", "motor model: ph14b, please `see <#>`_"
   "gripper motor", "|damiao_motor|", "2", "motor model: DM-J4310-2EC, please `see <#>`_"



Body structure components
-------------------------

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

.. |scapular| image:: ./_static/images/structure_components/scapular.png
   :align: middle
   :width: 100px
   :alt: the shoulder part is used to fix the front and rear chest plates

.. |head_plate| image:: ./_static/images/structure_components/head_plate.png
   :align: middle
   :width: 100px
   :alt: used to supporte head

.. |shoulder_left_plate| image:: ./_static/images/structure_components/shoulder_left_plate.png
   :align: middle
   :width: 100px
   :alt: shoulder motor connection plate

.. |shoulder_right_plate| image:: ./_static/images/structure_components/shoulder_right_plate.png
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
   "scapular", "|scapular|", "2", "used to fix the front and rear chest plates"
   "head plate", "|head_plate|", "1", "used for supporting head"
   "shoulder left plate", "|shoulder_left_plate|", "2", "shoulder motor connection left plate"
   "shoulder right plate", "|shoulder_right_plate|", "2", "shoulder motor connection right plate"
   "upper arm", "|upper_arm|", "2", "arm motor 2 and 3 connection component"
   "elbow left", "|elbow_left|", "2", "arm motor 3 and 4 connection component"
   "elbow right", "|elbow_right|", "2", "arm motor 3 and 4 connection component"
   "forearm left", "|forearm_left|", "2", "arm motor 4 and 5 connection component"
   "forearm right", "|forearm_right|", "2", "arm motor 4 and 5 connection component"
   "upper wrist", "|upper_wrist|", "2", "suite for arm motor 5"
   "wrist flange", "|wrist_flange|", "2", "flange for arm motor 5 and 6 connection"




Screws
------


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


.. |M8X20| image:: ./_static/images/screw/M8X20.png
   :align: middle
   :width: 100px
   :alt: M8X20


.. csv-table:: material statement for screws
   :header: "Name", "Image"
   :widths: 50, 50
   :class: white-background

   "M4X16", "|M4X16|"
   "M4X30", "|M4X30|"
   "M4X45", "|M4X45|"
   "M6X12", "|M6X12|"
   "M8X20", "|M8X20|"

Mechanical Components
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



.. csv-table:: material statement for tools
   :header: "Name", "Image", "Quantity", "Notes"
   :widths: 10, 30, 10, 50
   :class: white-background

   "screw glue", "|screw_glue|", "1", "used to prevent the screws from loosening"
   "hexagon wrench", "|hexagon_wrench|", "1", "used to tighten the screws"
   "torque wrench", "|torque_wrench|", "1", "set torque to avoid screw stripping"
   "vise", "|vise|", "1", "securely hold an object in place"
   "wire strippers", "|wire_strippers|", "1", "stripping wires"
   "locking pilers", "|locking_pilers|", "1", "pulling out pins"
   "diagonal pliers", "|diagonal_cutting_pliers|", "1", "cutting wires"
   "soldering fixture", "|soldering_station_fixture|", "1", "fix components and facilitate welding"



Power system
============================================
coming soon


CAN system
============================================
coming soon


Integration
============================================

This page will guide you through the process of assembling all components into the robot.



Waist Motor
-----------
The waist motor provides the robot with the ability to rotate left and right. Please follow the instructions to assemble.



Material Statement
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


Assemble Video(4X speed)
++++++++++++++++++++++++

.. video:: ./_static/videos/waist.mp4
   :width: 100%
   :autoplay:
   :loop:
   :muted:





Chest Motor
-----------
The chest provide with one freedom to turn up and down, what we need as follows. Please follow the instructions to assemble.


Material Statement
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



Assemble Video(4X speed)
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










