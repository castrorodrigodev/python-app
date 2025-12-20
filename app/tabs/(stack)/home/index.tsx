import CustomButton from '@/components/shared/custom-bottom';
import { Link, router } from 'expo-router';
import React from 'react';
import { Text, View } from 'react-native';

const Home = () => {
  return (
    <View className='flex-1 items-center justify-center bg-white'>
      <Text className='text-xl'>Welcome to Nativewind!</Text>
      <Text className='text-xl font-work-black text-primary'>
        Welcome to Nativewind!
      </Text>
      <Text className='text-xl font-work-medium text-secondary-100'>
        Welcome to Nativewind!
      </Text>
      <Text className='text-xl font-work-light text-secondary-200'>
        Welcome to Nativewind!
      </Text>
      <Text className='text-xl font-work-light text-tertiary'>
        Welcome to Nativewind!
      </Text>
      <CustomButton
        className='mt-10'
        color='primary'
        onPress={() => router.push('/tabs/(stack)/products')}
        onLongPress={() => {}}
      >
        Products
      </CustomButton>
      <Link href='/tabs/(stack)/profile' asChild>
        <CustomButton
          className='mt-5'
          variant='text-only'
          onLongPress={() => {}}
        >
          Profile
        </CustomButton>
      </Link>
      <Link href='/tabs/(stack)/settings' asChild>
        <CustomButton
          className='mt-5'
          variant='text-only'
          onLongPress={() => {}}
        >
          Settings
        </CustomButton>
      </Link>
    </View>
  );
};

export default Home;
