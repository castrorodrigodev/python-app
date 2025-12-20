import { Pressable, PressableProps, Text } from 'react-native';

interface ICustomButtonProps extends PressableProps {
  children: string;
  color?: 'primary' | 'secondary' | 'tertiary';
  onPress?: () => void;
  onLongPress: () => void;
  variant?: 'contained' | 'text-only';
  className?: string
}

const CustomButton = ({
  children,
  color = 'primary',
  variant = 'contained',
  className,
  onPress,
  onLongPress,
}: ICustomButtonProps) => {
  const btnColor = {
    primary: 'bg-primary',
    secondary: 'bg-secondary',
    tertiary: 'bg-tertiary',
  }[color];

  const textColor = {
    primary: 'text-primary',
    secondary: 'text-secondary',
    tertiary: 'text-tertiary',
  }[color];

  if (variant === 'text-only') {
    return (
      <Pressable className={`p-3 ${className}`} onPress={onPress}>
        <Text className={`text-center ${textColor}`}>{children}</Text>
      </Pressable>
    );
  }

  return (
    <Pressable
      className={`p-3 rounded-md ${btnColor} active:opacity-90 ${className}`}
      onPress={onPress}
      onLongPress={onLongPress}
    >
      <Text className='text-white text-center'>{children}</Text>
    </Pressable>
  );
};

export default CustomButton;
