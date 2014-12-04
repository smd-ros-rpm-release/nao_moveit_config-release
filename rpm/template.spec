Name:           ros-indigo-nao-moveit-config
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS nao_moveit_config package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-fake-controller-manager
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-moveit-simple-controller-manager
Requires:       ros-indigo-nao-description
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-nao-description

%description
An automatically generated package with all the configuration and launch files
for using the NAO robot with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 04 2014 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Wed Sep 24 2014 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Mikael Arguedas <assistant@moveit.ros.org> - 0.0.1-0
- Autogenerated by Bloom

