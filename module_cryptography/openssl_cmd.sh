#!/usr/bin/env bash

# ������Կ��
openssl genrsa -out mykey.pem 2048

# openssl genrsa -des3 -out mykey2.pem 2048

# ����Կ���з������Կ
openssl rsa -in mykey.pem -pubout -out mypubkey.pem

# openss rsa -in mykey2.pem -pubout -out mypubkey2.pem

# �����Կ���ļ��Ƿ���ȷ
openssl rsa -in mykey.pem -check -noout

# ��ʾ��Կ��Ϣ
openssl rsa -pubin -in mypubkey.pem -text

# ���������ļ�
echo "hello" >> plain.txt

# ʹ����Կ�Լ���
openssl rsautl -encrypt -inkey mykey.pem -in plain.txt -out cipher.txt
# ʹ�ù�Կ����
openssl rsautl -encrypt -pubin -inkey mypubkey.pem -in plain.txt -out cipher2.txt

# ����
openssl rsautl -decrypt -inkey mykey.pem -in cipher.txt

########## DH start
# ����һ�� 2014 ���صĲ����ļ�
openssl dhparam -out dhparam.pem -2 1024

# �鿴�����ļ�����
openssl dhparam -in dhparam.pem -noout -C

# ���ڲ����ļ�������Կ��
openssl genpkey -paramfile dhparam.pem -out dhkey.pem

# �鿴��Կ���ļ�����
openssl pkey -in dhkey.pem -text -noout

#### DH ��ԿЭ������
# ͨ��˫�����κ�һ������DH�Ĳ����ļ������Զ��⹫��
openssl genpkey -genparam -algorithm DH -out dhp.pem

# �鿴�����ļ������ݣ�����p��g�Ȳ���
openssl pkeyparam -in dhp.pem -text

# ���ͷ�A���ڲ����ļ�����һ����Կ��
openssl genpkey -paramfile dhp.pem -out akey.pem

# �鿴��Կ����
openssl pkey -in akey.pem -text -noout

# ���ͷ�B���ڲ����ļ�����һ����Կ��
openssl genpkey -paramfile dhp.pem -out bkey.pem

# �鿴��Կ������
openssl pkey -in bkey.pem -text -noout

# ���ͷ�A�����Կ�ļ�akey_pub.pem��˽Կ�Լ�����
openssl pkey -in akey.pem -pubout -out akey_pub.pem

# ���ͷ�B�����Կ�ļ�bkey_pub.pem��˽Կ�Լ�����
openssl pkey -in bkey.pem -pubout -out bkey_pub.pem

# ���ͷ�A�յ�B���͹����Ĺ�Կ����Э�̳�����Կ���浽data_a.txt�ļ���
openssl pkeyutl -derive -inkey akey.pem -peerkey bkey_pub.pem -out data_a.txt

# ���ͷ�B�յ�A���͹����Ĺ�Կ����Э�̳�����Կ���浽data_b.txt�ļ���
openssl pkeyutl -derive -inkey bkey.pem -peerkey akey_pub.pem -out data_b.txt

# �鿴ϵͳ�ж�����Բ����
openssl ecparam -list_curves

# ����һ�������ļ���ͨ��-nameָ����������
openssl ecparam -name secp256k1 -out secp25k1.pem

# Ĭ������£��鿴�����ļ�ֻ����ʵ���ߵ�����
openssl ecparam -in secp25k1.pem -text -noout

# ��ʵ�����ļ���ľ������
openssl ecparam -in secp25k1.pem -text -param_enc explicit -noout

# RSAǩ��������RSA��Կ��
openssl genrsa -out rsaprivatekey.pem 1024

# RSAǩ��������Կ������ȡ����Կ
openssl rsa -in rsaprivatekey.pem -pubout -out rsapublickey.pem

# ��plain.txtʹ��sha256��ϣ�㷨��ǩ���㷨������ǩ���ļ�signature.txt
openssl dgst -sha256 -sign rsaprivatekey.pem -out signature.txt plain.txt

# ��Ӧ����ǩ����
openssl dgst -sha256 -verify rsapublickey.pem -signature signature.txt plain.txt


### DSA�㷨ʵ��
# ���ɲ����ļ���������DH�����ļ�
openssl dsaparam -out dsaparam.pem 1024

# ͨ�������ļ�������Կ�� dsaprivatekey.pem
openssl gendsa -out dsaprivatekey.pem dsaparam.pem

# ��˽Կ�ļ�ʹ��des3�㷨���м���
openssl gendsa -out dsaprivatekey2.pem -des3 dsaparam.pem

# ͨ����Կ���ļ�����ֳ���Կ
openssl dsa -in dsaprivatekey.pem -pubout -out dsapublickey.pem

# ��ʾ˽Կ�ļ���Ϣ
openssl dsa -in dsaprivatekey.pem -text

# ��ʾ��Կ���ļ�����Ϣ
openssl dsa -pubin -in dsapublickey.pem -text

# dsaǩ��
openssl dgst -sha256 -sign dsaprivatekey.pem -out signature.txt plain.txt

# dsa��ǩ
openssl dgst -sha256 -verify dsapublickey.pem -signature signature.txt plain.txt

# ����ECDSA˽Կ
openssl ecparam -name secp256k1 -genkey -out ecdsa_priv.pem

# ��ʾECDSA˽Կ��Ϣ
openssl ec -in ecdsa_priv.pem -text -noout

# ��ȡECDSA��Կ
openssl ec -in ecdsa_priv.pem -pubout -out ecdsa_pub.pem

# ��ʾECDSA��Կ��Ϣ
openssl ec -in ecdsa_pub.pem -pubin -text -noout

# ʹ��ECDSAǩ��
openssl dgst -sha256 -sign ecdsa_priv.pem -out signature.txt plain.txt

# ECDSA��ǩ
openssl dgst -sha256 -verify ecdsa_pub.pem -signature signature.txt plain.txt

# ���ܲ���
openssl speed aes-128-cbc

# ���ܲ��ԣ�����EVPģʽ
openssl speed -evp aes-128-cbc

# ����˽Կ�Ժ�CSR
openssl req -newkey rsa:1024 -nodes -keyout example_key.pem -out example_csr.pem

# ������ǩ��֤��
openssl x509 -signkey example_key.pem -in example_csr.pem -req -days 365 -out example_cert.pem
