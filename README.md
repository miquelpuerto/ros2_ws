# ros2_ws

Intended folder structure:
leo_autoware_project/
├── .git/                     # Directorio de Git
├── .gitignore                # Especifica qué archivos ignorar (muy importante)
├── README.md                 # Descripción del proyecto, cómo empezar, etc.
|
├── autoware.repos            # Archivo para vcs tool, define qué repositorios de Autoware y qué versiones usar
|
├── src/                      # Directorio raíz de tu workspace de colcon donde irá TU CÓDIGO y Autoware
│   │
│   ├── leo_vehicle_interface/  # TU PAQUETE ROS 2 PERSONALIZADO
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── leo_vehicle_interface/ # Directorio del paquete Python
│   │   │   └── vehicle_interface_node.py # Tu nodo de interfaz
│   │   ├── launch/
│   │   │   └── vehicle_interface.launch.py
│   │   └── params/
│   │       └── leo_rover.param.yaml # Parámetros como WHEELBASE
│   │
│   ├── leo_sensor_kit_bringup/ # TU PAQUETE ROS 2 PERSONALIZADO
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── launch/             # Launch files para tus sensores (Lidar, Cámara, RTK)
│   │   │   ├── lidar.launch.py
│   │   │   ├── camera.launch.py
│   │   │   └── rtk_gps.launch.py
│   │   └── params/             # Archivos de configuración para tus sensores
│   │       ├── lidar_config.yaml
│   │       └── camera_info.yaml
│   │
│   ├── leo_description/        # TU PAQUETE ROS 2 PERSONALIZADO (Opcional, para URDF)
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── urdf/
│   │   │   └── leo_rover_with_sensors.urdf.xacro
│   │   ├── meshes/
│   │   └── rviz/
│   │       └── display.rviz
│   │
│   ├── (Opcional) leo_custom_planning/ # Si desarrollas algoritmos de planning propios
│   │   └── ...
│   │
│   └── (Aquí es donde `vcs import` clonaría los repositorios de Autoware definidos en autoware.repos)
│       ├── autoware.universe/
│       ├── autoware.common/
│       └── ... (otros repos de Autoware)
│
├── launch/                   # Archivos de lanzamiento de nivel superior para todo el sistema
│   └── leo_autoware.launch.py  # Lanza Autoware y tus nodos personalizados
│
├── config/                   # Configuraciones globales o específicas del vehículo para Autoware
│   ├── vehicle/                # Parámetros del vehículo para Autoware
│   │   └── vehicle_info.param.yaml # Dimensiones, límites, etc., que Autoware necesita
│   ├── sensors/              # Calibraciones de sensores (extrínsecos)
│   │   └── sensor_kit_calibration.yaml
│   └── maps/                   # Archivos de mapas (PCD, Lanelet2) o scripts para generarlos/descargarlos
│       └── (Podría ser mejor gestionar mapas grandes fuera de Git)
│
├── docker/                   # Si usas Docker para el despliegue en el Jetson Orin
│   ├── Dockerfile.jetson_autoware
│   └── docker-compose.yml    # (Opcional)
│
├── scripts/                  # Scripts útiles (ej: setup del Jetson, descarga de artefactos, etc.)
│   └── setup_jetson_orin.sh
│
└── docs/                     # Documentación específica de tu proyecto
    ├── architecture.md
    └── setup_guide.md