data segment
        a db ?
        msg db "Enter first num $"
        msg1 db "Enter second num $"
        msg2 db "Addition is $"
        newl db 0Ah,0Dh,"$"
data ends

code segment
assume cs:code,ds:data

start:

mov ax,data
mov ds,ax

mov dx,OFFSET msg
mov ah,09h
int 21h

call input
mov a,bl

mov dx,OFFSET newl
mov ah,09h
int 21h



mov dx,OFFSET msg1
mov ah,09h
int 21h

call input

mov dx,OFFSET newl
mov ah,09h
int 21h

        mov dx,OFFSET msg2
        mov ah,09h
        int 21h

        mov cl,00
        add bl,a
        jnc i3
        inc cl

i3:     mov dh,bl
        mov bl,cl
        and bl,0FH
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0F0h
        ror bl,04h

        call convert
        mov dl,bl
        mov ah,02h
        int 21h

        mov bl,dh
        and bl,0fh
        call convert

        mov dl,bl
        mov ah,02h
        int 21h

mov ah,4ch
int 21h

input proc
        mov ah,01h
        int 21h

        call ascii2hex
        mov bl,al
        rol bl,4

        mov ah,01h
        int 21h
        call ascii2hex
        add bl,al
        ret
        endp

ascii2hex proc
        cmp al,41H
        jc num
        sub al,07h
        num:sub al,30h
        ret
        endp

convert proc
        cmp bl,0ah
        jc i1
        add bl,37h
        jmp i2
        i1:add bl,30h
        i2:ret
        endp

code ends
end start

