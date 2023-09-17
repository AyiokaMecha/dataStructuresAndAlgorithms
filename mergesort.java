public class MergeSort{
    public static void main(string[] args){
        int[] data=new int[]{-5,20,10,7,8,9,50,34,23,12,23};
        mergeSort(data,0,data.length-1);
        System.out.print("Stop");
    }

    public static void MergeSort(int[] data,int start, int end){
        if(start<end){
            int mid=(start+end)/2;
            mergeSort(data,start,mid);
            mergeSort(data,mid+1,end);
            merge(data,start,mid,end);
        }
    }



    public static void merge(int[] data, int start,int mid, int end){
         //building a temporary array
         int[] temp=new int[end-start+1];
         int  i=start,j=mid+1,k=0;
         while(i<=mid && j<=end){
         if(data[i]<data[j]){
            temp[k++]=data[i++];
         }
         else{
            temp[k++]=data[j++];
         }}
         while(i<=mid){
            temp[k++]=data[i++];
         }
         while(j<=end){
            temp[k++]=data[j++];
         }

         for(i=start,1<=end,i++){
            data[i]=temp[i-start];
         }
    }
}