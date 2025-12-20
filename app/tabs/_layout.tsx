import FontAwesome from '@expo/vector-icons/FontAwesome';
import { Tabs } from 'expo-router';

const TabsLayout = () => {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: 'blue',
        headerShown: false,
        tabBarStyle: {
          backgroundColor: 'black',
        },
      }}
    >
      <Tabs.Screen
        name='(stack)'
        options={{
          title: 'Stack',
          tabBarIcon: ({ color }) => (
            <FontAwesome size={28} name='user' color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name='home/index'
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => (
            <FontAwesome size={28} name='home' color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name='favorites/index'
        options={{
          title: 'Favorites',
          tabBarIcon: ({ color }) => (
            <FontAwesome size={28} name='cog' color={color} />
          ),
        }}
      />
    </Tabs>
  );
  // const scheme = useColorScheme();
  // const tabColor = scheme === 'dark' ? '#fff' : '#000';

  // return (
  //   <NativeTabs labelStyle={{ color: tabColor }} tintColor={tabColor}>
  //     <NativeTabs.Trigger name='home/index'>
  //       <Label>Home</Label>
  //       <Icon sf='house.fill' drawable='custom_android_drawable' />
  //     </NativeTabs.Trigger>
  //     <NativeTabs.Trigger name='favorites/index'>
  //       <Icon sf='gear' drawable='custom_settings_drawable' />
  //       <Label>Favorites</Label>
  //     </NativeTabs.Trigger>
  //   </NativeTabs>
  // );
};

export default TabsLayout;
