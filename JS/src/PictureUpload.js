import React, { useState } from 'react';
import { View, Text, Button, Image, StyleSheet } from 'react-native';
import ImagePicker from 'react-native-image-picker';
import axios from 'axios';

const PictureUpload = () => {
  const [image, setImage] = useState(null);

  const selectImage = () => {
    ImagePicker.showImagePicker({}, response => {
      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.error) {
        console.log('ImagePicker Error: ', response.error);
      } else {
        const source = { uri: response.uri };
        setImage(source);
        uploadImage(response.uri);
      }
    });
  };

  const uploadImage = async uri => {
    const apiUrl = 'http://localhost:3000/upload';
    const formData = new FormData();
    formData.append('photo', {
      uri,
      type: 'image/jpeg',
      name: 'photo.jpg',
    });
    const options = {
      headers: {
        Accept: 'application/json',
        'Content-Type': 'multipart/form-data',
      },
    };
    try {
      const response = await axios.post(apiUrl, formData, options);
      console.log('upload success', response.data);
    } catch (error) {
      console.log('upload error', error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Picture Upload</Text>
      {image && <Image source={image} style={styles.image} />}
      <Button title="Select Picture" onPress={selectImage} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 20,
  },
});

export default PictureUpload;
