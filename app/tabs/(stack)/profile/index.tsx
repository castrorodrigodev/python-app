import { Link } from 'expo-router';
import React from 'react';
import { Text, View } from 'react-native';

const Profile = () => {
  return (
    <View className='flex-1 items-center justify-center bg-white'>
      <Text className='text-xl'>Welcome to Profile</Text>
      <Link href='/tabs/(stack)/home'>Go to Home</Link>
      <Link href='/tabs/(stack)/products'>Go to Products</Link>
      <Link href='/tabs/(stack)/settings'>Go to Settings</Link>
    </View>
  );
};

export default Profile;
