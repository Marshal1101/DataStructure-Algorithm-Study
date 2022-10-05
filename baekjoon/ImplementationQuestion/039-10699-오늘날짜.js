let KST = new Date();
console.log(KST.getFullYear() + "-" + (KST.getMonth()+1).toString().padStart(2, '0') + "-" + KST.getDate().toString().padStart(2, '0'));