import CustomDrawer from '@/components/shared/custom-bottom/custom-drawer';
import FontAwesome from '@expo/vector-icons/FontAwesome';
import { Drawer } from 'expo-router/drawer';
import React from 'react';

const DrawerLayout = () => {
  return (
    <Drawer
      drawerContent={CustomDrawer}
      screenOptions={{
        overlayColor: 'rgba(0,0,0,0.4)',
        drawerActiveTintColor: 'indigo',
        headerShadowVisible: false,
        sceneStyle: {
          backgroundColor: 'white',
        },
      }}
    >
      <Drawer.Screen
        name='terms/index'
        options={{
          drawerLabel: 'Terms',
          title: 'Terms',
          drawerIcon: ({ color, size }) => (
            <FontAwesome name='user' size={size} color={color} />
          ),
        }}
      />
      <Drawer.Screen
        name='heroes/index'
        options={{
          drawerLabel: 'Heroes',
          title: 'Heroes',
          drawerIcon: ({ color, size }) => (
            <FontAwesome name='cog' size={size} color={color} />
          ),
        }}
      />
    </Drawer>
  );
};

export default DrawerLayout;
