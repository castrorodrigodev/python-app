import { Redirect } from 'expo-router';

export default function App() {
  // return <Redirect href='/(stack)/home' />;
  // return <Redirect href='./tabs' />;
  return <Redirect href='./drawer' />;
  // return (
  //   <View className='flex-1 items-center justify-center bg-white'>
  //     <Text className='text-xl'>Welcome to Nativewind!</Text>
  //     <Text className='text-xl font-work-black text-primary'>
  //       Welcome to Nativewind!
  //     </Text>
  //     <Text className='text-xl font-work-medium text-secondary-100'>
  //       Welcome to Nativewind!
  //     </Text>
  //     <Text className='text-xl font-work-light text-secondary-200'>
  //       Welcome to Nativewind!
  //     </Text>
  //     <Text className='text-xl font-work-light text-tertiary'>
  //       Welcome to Nativewind!
  //     </Text>

  //     <CustomButton
  //       className='mt-10'
  //       color='primary'
  //       onPress={() => router.push('/products')}
  //       onLongPress={() => {}}
  //     >
  //       Products
  //     </CustomButton>

  //     <Link href='/profile' asChild>
  //       <CustomButton
  //         className='mt-5'
  //         variant='text-only'
  //         onLongPress={() => {}}
  //       >
  //         Profile
  //       </CustomButton>
  //     </Link>

  //     <Link href='/settings' asChild>
  //       <CustomButton
  //         className='mt-5'
  //         variant='text-only'
  //         onLongPress={() => {}}
  //       >
  //         Settings
  //       </CustomButton>
  //     </Link>
  //   </View>
  // );
}
