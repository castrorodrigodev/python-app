import { Link } from 'expo-router';
import { Text, View } from 'react-native';

const Settings = () => {
  return (
    <View className='flex-1 items-center justify-center bg-white'>
      <Text className='text-xl'>Welcome to Settings</Text>
      <Link href='/tabs/(stack)/profile'>Go to Profile</Link>
      <Link href='/tabs/(stack)/home'>Go to Home</Link>
    </View>
  );
};

export default Settings;
